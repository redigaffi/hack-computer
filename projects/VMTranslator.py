import sys
import re
from typing import Optional
import config
config.file_name = sys.argv[1]
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

lines = load_file_and_cleanup(config.file_name)
tokens = tokenize(lines)
asm = generate_hack_asm(tokens)
write_to_file(f"{config.file_name.split('.')[0]}.asm", asm)
