#TODO: Need to keep track of labels and create different names, just like static
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import sys
import config

# Keep track of static memory segment symbols, ex: @Foo.i where Foo is the file name and i is the counter
static_symbol_list = []
jump_counter = 0

# Contains e.g:
# FileName$ret => 0, 1, 2 for each return entry the function has, the value is incremented
function_return_jumps = {}

class OpCodes(str, Enum):
    C_ADD = 'add'
    C_SUB = 'sub'
    C_NEG = 'neg'
    C_EQ = 'eq'
    C_GT = 'gt'
    C_LT = 'lt'
    C_AND = 'and'
    C_OR = 'or'
    C_NOT = 'not'
    C_PUSH = 'push'
    C_POP = 'pop'
    C_LABEL = 'label'
    C_GOTO = 'goto'
    C_IF = 'if-goto'
    C_FUNCTION = 'function'
    C_RETURN = 'return'
    C_CALL = 'call'

class MemorySegments(str, Enum):
    M_LOCAL = 'local'
    M_ARGUMENT = 'argument'
    M_THIS = 'this'
    M_THAT = 'that'
    M_POINTER = 'pointer'
    M_TEMP = 'temp'
    M_CONSTANT = 'constant'
    M_STATIC = 'static'


memory_segment_asm_label_mapping = {
    MemorySegments.M_LOCAL: '@LCL',
    MemorySegments.M_ARGUMENT: '@ARG',
    MemorySegments.M_THIS: '@THIS',
    MemorySegments.M_THAT: '@THAT',
}

@dataclass
class Operation:
    raw_line: str
    opcode: OpCodes
    segment: Optional[MemorySegments|str]
    index: Optional[int]

def handle_memory_segment_pointer(op: Operation) -> str:
    assert op.segment == MemorySegments.M_POINTER, f"Passed memory segment to handle_memory_segment_pointer is wrong: {op.segment}"
    label = "@THIS" if op.index == 0 else "@THAT"
    ret = f"""{label}"""
    return ret

def handle_memory_segment_available_labels(op: Operation) -> str:
    assert op.segment in [MemorySegments.M_LOCAL, MemorySegments.M_ARGUMENT, MemorySegments.M_THIS, MemorySegments.M_THAT], f"Passed memory segment to handle_memory_segment_available_labels is wrong: {op.segment}"
    label = memory_segment_asm_label_mapping.get(op.segment)
    ret = f"""
@{op.index}
D=A
{label}
A=D+M"""
    return ret

def handle_memory_segment_temp(op: Operation) -> str:
    tmp_segment_base_addr = 5 # 5-12
    addr = tmp_segment_base_addr + int(op.index) # base_address + offset
    ret = f"""@{addr}"""
    return ret

def handle_memory_segment_static(op: Operation) -> str:
    global static_reference_counter
    global static_symbol_list

    file_name = config.file_name.split(".")[0]
    symbol_name = f"@{file_name}.{op.index}"
    asm = f"""{symbol_name}"""
    static_symbol_list.append(symbol_name)
    return asm 

def handle_memory_segments(op: Operation) -> str:
    if op.segment == MemorySegments.M_POINTER:
        return handle_memory_segment_pointer(op)
    elif op.segment in [MemorySegments.M_LOCAL, MemorySegments.M_ARGUMENT, MemorySegments.M_THIS, MemorySegments.M_THAT]:
        return handle_memory_segment_available_labels(op)
    elif op.segment == MemorySegments.M_TEMP:
        return handle_memory_segment_temp(op)
    elif op.segment == MemorySegments.M_STATIC:
        return handle_memory_segment_static(op)

    raise RuntimeError(f"Memory segment {op.segment} not implemented")

# TODO: This can be optimized, we know the value of memory segment (ie @LCL -> 300), so we can
# calculate the address at compile time (offset + index) 
class Op_Pop():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_POP, "Operation passed to C_Pop is wrong"
        self.operation = operation

    def __str__(self) -> str:
        if self.operation.segment == MemorySegments.M_CONSTANT:
            print("Cant pop to constant memory segment")
            sys.exit(1)
        else:
            mem_segment = handle_memory_segments(self.operation)

            return f"""
{mem_segment}
D=A
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
//SP--
@SP
M=M-1"""      

class Op_Push():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_PUSH, "Operation passed to C_Push is wrong"
        self.operation = operation

    def __str__(self) -> str:
        if self.operation.segment == MemorySegments.M_CONSTANT:
            return f"""
@{self.operation.index}
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1"""
        else:
            mem_segment = handle_memory_segments(self.operation)
            return f"""
{mem_segment}
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1"""

class Op_Add():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_ADD, "Operation passed to C_Add is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
D=M
A=A-1
D=M+D
@SP
A=M-1
A=A-1
M=D
//SP--
@SP
M=M-1"""

class Op_Sub():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_SUB, "Operation passed to C_Sub is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
D=M
A=A-1
D=M-D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D
//SP--
@SP
M=M-1"""

class Op_Neg():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_NEG, "Operation passed to C_Neg is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
D=!M
D=D+1
// STACK[SP-1] = D
@SP
A=M-1
M=D"""

class Op_Eq():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_EQ, "Operation passed to C_Eq is wrong"
        self.operation = operation

    def __str__(self) -> str:
        global jump_counter
        jump_name = f"JUMP_{jump_counter}"
        jump_counter += 1
        return f"""
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-1] - STACK[SP-2]
D=D-M
@{jump_name}

// if D == 0 jump to EQUAL
D;JEQ

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@{jump_name}_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
({jump_name})
@SP
A=M-1
A=A-1
M=-1
({jump_name}_END)

// SP--
@SP
M=M-1"""

class Op_Gt():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_GT, "Operation passed to C_Gt is wrong"
        self.operation = operation

    def __str__(self) -> str:
        global jump_counter
        jump_name = f"JUMP_{jump_counter}"
        jump_counter += 1
        return f"""
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D
@{jump_name}

// if D > 0 jump to GREATER
D;JGT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@{jump_name}_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
({jump_name})
@SP
A=M-1
A=A-1
M=-1
({jump_name}_END)

// SP--
@SP
M=M-1"""

class Op_Lt():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_LT, "Operation passed to C_Lt is wrong"
        self.operation = operation

    def __str__(self) -> str:
        global jump_counter
        jump_name = f"JUMP_{jump_counter}"
        jump_counter += 1
        return f"""
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D

// if D < 0 jump to GREATER
@{jump_name}
D;JLT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@{jump_name}_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
({jump_name})
@SP
A=M-1
A=A-1
M=-1
({jump_name}_END)

// SP--
@SP
M=M-1"""

class Op_And():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_AND, "Operation passed to C_And is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] & STACK[SP-1]
D=M&D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D

// SP--
@SP
M=M-1"""

class Op_Or():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_OR, "Operation passed to C_Or is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] | STACK[SP-1]
D=M|D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D

// SP--
@SP
M=M-1"""

class Op_Not():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_NOT, "Operation passed to C_Not is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@SP
A=M-1
M=!M"""

class Op_Function():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_FUNCTION, "Operation passed to C_Function is wrong"
        self.operation = operation

    def __str__(self) -> str:
        push = f"""
// push 0
@0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
""" * self.operation.index

        return f"""
({self.operation.segment})
{push}"""

class Op_Return():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_RETURN, "Operation passed to C_Return is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
// endFrame = LCL
@LCL
D=M
@endFrame
M=D

//retAddr = *(endFrame - 5)
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
M=D

//*ARG = pop
@SP
A=M-1
D=M
@ARG
A=M
M=D

// SP = ARG + 1 
@ARG
D=M+1
@SP
M=D

// THAT = *(endFrame - 1)
@1
D=A
@endFrame
D=M-D
A=D
D=M
@THAT
M=D

// THIS = *(endFrame - 2)
@2
D=A
@endFrame
D=M-D
A=D
D=M
@THIS
M=D

// ARG = *(endFrame - 3)
@3
D=A
@endFrame
D=M-D
A=D
D=M
@ARG
M=D

// LCL = *(endFrame - 4)
@4
D=A
@endFrame
D=M-D
A=D
D=M
@LCL
M=D

// goto retAddr
@retAddr
A=M
0;JMP"""

class Op_Call():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_CALL, "Operation passed to C_Call is wrong"
        self.operation = operation

    def __str__(self) -> str:
        file_name = config.file_name.split(".")[0]
        return_entry = function_return_jumps.get(f"{file_name}$ret", 0)
        function_return_jumps[f"{file_name}$ret"] = return_entry + 1
        label_name = f"{file_name}$ret.{return_entry}"
        return f"""
// push return address to stack
@{label_name}
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push LCL
@LCL
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push ARG
@ARG
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THIS 
@THIS
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THAT 
@THAT
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//ARG = SP-5-nArgs
@{self.operation.index}
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@{self.operation.segment}
0;JMP
({label_name})"""

class Op_Label():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_LABEL, "Operation passed to C_Label is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
({self.operation.segment})"""

class Op_Goto():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_GOTO, "Operation passed to C_Goto is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
@{self.operation.segment}
0;JMP
"""


class Op_IfGoto():
    operation: Operation

    def __init__(self, operation: Operation):
        assert operation.opcode == OpCodes.C_IF, "Operation passed to C_If is wrong"
        self.operation = operation

    def __str__(self) -> str:
        return f"""
//D = *SP
@SP
A=M-1
D=M

//SP--
@SP
M=M-1

// if D > 0 JUMP
@{self.operation.segment}
D;JGT
"""

opcode_asm_mapping = {
    OpCodes.C_PUSH: Op_Push,
    OpCodes.C_POP: Op_Pop,
    OpCodes.C_ADD: Op_Add,
    OpCodes.C_SUB: Op_Sub,
    OpCodes.C_NEG: Op_Neg,
    OpCodes.C_EQ: Op_Eq,
    OpCodes.C_GT: Op_Gt,
    OpCodes.C_LT: Op_Lt,
    OpCodes.C_AND: Op_And,
    OpCodes.C_OR: Op_Or,
    OpCodes.C_NOT: Op_Not,
    OpCodes.C_FUNCTION: Op_Function,
    OpCodes.C_RETURN: Op_Return,
    OpCodes.C_CALL: Op_Call,
    OpCodes.C_LABEL: Op_Label,
    OpCodes.C_GOTO: Op_Goto,
    OpCodes.C_IF: Op_IfGoto,
}
