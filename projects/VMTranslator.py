import sys
import os
import re
from typing import Optional
import config
config.file_name = sys.argv[1]
config.arg1 = sys.argv[1]
from op import Operation, OpCodes, MemorySegments, opcode_asm_mapping

def load_file_and_cleanup(path) -> list[str]:
    with open(path, "r") as hack_vm_file:
        lines = []
        for line in hack_vm_file:
            if line and line.isspace() and line.strip():
                continue

            if len(line) == 1 and ord(line) == 10:
                continue

            if line[0:2] == "//":
                continue
            
            # Remove line comments
            removed_comments = re.sub("(\/\/.*)", "", line)
            removed_new_line = removed_comments.rstrip("\n")
            cleaned = removed_new_line.strip()

            lines.append(cleaned)

        return lines

def tokenize(lines: list[str]) -> list[Operation]:
    operations = []
    for line in lines:
        args = line.split(" ")
        if len(args) == 3:
           opcode = OpCodes(args[0])
           second_param  = args[1]

           if opcode in [opcode.C_PUSH, opcode.C_PUSH]:
                second_param = MemorySegments(args[1])

           operation = Operation(line, opcode, second_param, int(args[2])) 
        elif len(args) == 2:
           opcode = OpCodes(args[0])
           second_param  = args[1]
           operation = Operation(line, opcode, second_param, None) 

        else:
           operation = Operation(line, OpCodes(args[0]), None, None) 

        operations.append(operation)
    return operations

def generate_hack_asm(tokens: list[Operation]) -> str:
    output = ""
    for token in tokens:
        token_to_asm_mapper = opcode_asm_mapping.get(token.opcode)
        output += f"//{token.raw_line}"
        mapper = token_to_asm_mapper(token)
        output += str(mapper) + "\n"
                
    return output

def write_to_file(file_name: str, machine_code: str) -> None:
    with open(file_name, 'w') as f:
        f.write(machine_code)


# def bootstrap_code() -> str:
#     return f"""
# // Bootstrap
# @256
# D=A
# @SP
# M=D
# @Sys.init
# 0;JMP
# """

def bootstrap_code() -> str:
    return f"""
// Bootstrap
// Set stack pointer
@256
D=A
@SP
M=D

// push return address to stack
@Bootstrap$ret.0
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

//ARG = SP-5-nArgs (no args)
@5
D=A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@Sys.init
0;JMP
(Bootstrap$ret.0)
"""

asm_content = bootstrap_code()
path = f"{config.arg1.split('.')[0]}.asm"

if os.path.isfile(config.arg1):
    lines = load_file_and_cleanup(config.arg1)
    tokens = tokenize(lines)
    asm_content = generate_hack_asm(tokens)
else:
    folder = config.arg1
    if config.arg1[-1] == "/":
        config.arg1 = config.arg1[:-1] 

    file_name = config.arg1.split('/')[-1]
    path = f"{folder}/{file_name}.asm"
    
    for filename in os.scandir(config.arg1):
        if filename.is_file():
            ext = filename.name.split('.')[-1]
            if ext != 'vm':
                continue

            config.file_name = filename.name.split('.')[0]
            lines = load_file_and_cleanup(filename.path)
            tokens = tokenize(lines)
            asm_content += generate_hack_asm(tokens)


write_to_file(path, asm_content)
