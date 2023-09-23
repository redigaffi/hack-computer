import re
from abc import abstractmethod, ABC
from dataclasses import dataclass

symbol_table = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
}

var_location = 16

def load_file_and_cleanup(path) -> list[str]:
    with open(path, "r") as hack_asm_file:
        lines = []
        for line in hack_asm_file:
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

        hack_asm_file.close()
        return lines

def parse_label_symbols(parsed_lines: list[str]) -> list[str]:
        lines = []
        line_number = 0
        for line in parsed_lines:
            # Resolve label symbols
            if re.search("\(.*\)", line):
                label_name = line.replace("(", "")
                label_name = label_name.replace(")", "")

                if symbol_table.get(label_name) != None:
                    print("Label already exists")

                symbol_table[label_name] = line_number
                continue

            lines.append(line)
            line_number += 1

        return lines

def parse_variables_symbols(parsed_lines: list[str]) -> list[str]:
        global var_location
        lines = []
        for line in parsed_lines:
            if re.search("@[A-Za-z][A-Za-z]*", line):
                var_name = line.replace("@", "")
                if symbol_table.get(var_name) == None:
                    symbol_table[var_name] = var_location
                    var_location += 1

            lines.append(line)
            
        return lines

compute_functions = {
    "0": {
        "binary": "101010",
        "a": "0",
        "info": "0 constant"
    },
    "1": {
        "binary": "111111",
        "a": "0",
        "info": "1 constant"
    },
    "-1": {
        "binary": "111010",
        "a": "0",
        "info": "-1 constant"
    },
    "D": {
        "binary": "001100",
        "a": "0",
        "info": "D"
    },
    "A": {
        "binary": "110000",
        "a": "0",
        "info": "D"
    },
    "M": {
        "binary": "110000",
        "a": "1",
        "info": "M"
    },
    "!D": {
        "binary": "001101",
        "a": "0",
        "info": "!D"
    },
    "!A": {
        "binary": "110001",
        "a": "0",
        "info": "!A"
    },
    "!M": {
        "binary": "110001",
        "a": "1",
        "info": "!M"
    },
    "-D": {
        "binary": "001111",
        "a": "0",
        "info": "-D"
    },
    "-A": {
        "binary": "110011",
        "a": "0",
        "info": "-A"
    },
    "-M": {
        "binary": "110011",
        "a": "1",
        "info": "-M"
    },
    "D+1": {
        "binary": "011111",
        "a": "0",
        "info": "D+1"
    },
    "A+1": {
        "binary": "110111",
        "a": "0",
        "info": "A+1"
    },
    "M+1": {
        "binary": "110111",
        "a": "1",
        "info": "A+1"
    },
    "D-1": {
        "binary": "001110",
        "a": "0",
        "info": "D-1"
    },
    "A-1": {
        "binary": "110010",
        "a": "0",
        "info": "A-1"
    },
    "M-1": {
        "binary": "110010",
        "a": "1",
        "info": "M-1"
    },
    "D+A": {
        "binary": "000010",
        "a": "0",
        "info": "D+A"
    },
    "M+D": {
        "binary": "000010",
        "a": "1",
        "info": "M+D"
    },
    "D+M": {
        "binary": "000010",
        "a": "1",
        "info": "D+M"
    },
    "D-A": {
        "binary": "010011",
        "a": "0",
        "info": "D-A"
    },
    "D-M": {
        "binary": "010011",
        "a": "1",
        "info": "D-M"
    },
    "A-D": {
        "binary": "000111",
        "a": "0",
        "info": "A-D"
    },
    "M-D": {
        "binary": "000111",
        "a": "1",
        "info": "M-D"
    },
    "D&A": {
        "binary": "000000",
        "a": "0",
        "info": "D&A"
    },
    "D&M": {
        "binary": "000000",
        "a": "1",
        "info": "D&M"
    },
    "D|A": {
        "binary": "010101",
        "a": "0",
        "info": "D|A"
    },
    "D|M": {
        "binary": "010101",
        "a": "1",
        "info": "D|A"
    },
}

dest_table = {

    "null": {
        "binary": "000"
    },
    "M": {
        "binary": "001"
    },
    "D": {
        "binary": "010"
    },
    "MD": {
        "binary": "011"
    },

    "A": {
        "binary": "100"
    },
    "AM": {
        "binary": "101"
    },
    "AD": {
        "binary": "110"
    },
    "AMD": {
        "binary": "111"
    },
}

jump_table = {
    "null": {
        "binary": "000"
    },
    "JGT": {
        "binary": "001"
    },
    "JEQ": {
        "binary": "010"
    },
    "JGE": {
        "binary": "011"
    },

    "JLT": {
        "binary": "100"
    },
    "JNE": {
        "binary": "101"
    },
    "JLE": {
        "binary": "110"
    },
    "JMP": {
        "binary": "111"
    },
}

class Instruction(ABC):
    def to_machine_code(self) -> str:
        pass

@dataclass
class AInstruction(Instruction):
    raw: str
    value: int 

    def to_machine_code(self) -> str:
        bin_value = "0" + format(self.value, '015b')
        assert len(bin_value) == 16, "AInstruction not 16 bits long"
        return bin_value

@dataclass
class CInstruction(Instruction):
    raw: str
    dest: str
    comp: str
    jump: str

    def to_machine_code(self) -> str:
        binary_string = "111"

        compute_info = compute_functions.get(self.comp)
        dst_info = dest_table.get(self.dest)
        jmp_info = jump_table.get(self.jump)

        if compute_info:
            binary_string += compute_info["a"]
            binary_string += compute_info["binary"]
        else:
            print(f"No compute info found for: {self.comp}")
            binary_string += "0000000" # a + compute

        if dst_info:
            binary_string += dst_info["binary"]
        else:
            binary_string += "000"
        
        if jmp_info:
            binary_string += jmp_info["binary"]
        else:
            binary_string += "000"

        assert len(binary_string) == 16, "CInstruction not 16 bits long"
        return binary_string 

def parse_instructions(lines: list[str]) -> list:
    instructions = []

    for line in lines:

        # A instruction
        if line[0] == '@':
            value = line[1:]

            # Nothing to resolve, number constant
            if value.isdigit():
                instructions.append(AInstruction(line, int(value)))
            else:
                # We have to resolve the text constant
               data = symbol_table.get(value) 
               instructions.append(AInstruction(line, data))

            continue
        
        # C instruction
        tmp_line = line
        dest, comp, jump = "", "", ""
        if "=" in tmp_line:
            dest = tmp_line.split("=").pop(0)
            tmp_line = tmp_line.replace(f"{dest}=", "")
        
        if ";" in tmp_line:
            split = tmp_line.split(";")
            comp = split.pop(0)

            tmp_line = tmp_line.replace(f"{comp};", "")
            if len(split) > 0:
                jump = split.pop(0)
                tmp_line = tmp_line.replace(f"{jump}", "")
        else:
            comp = tmp_line

        instruction = CInstruction(line, dest, comp, jump)
        instructions.append(instruction)

    return instructions

def generate_hack_machine_code(instructions: list) -> None:
    machine_code = []

    for instruction in instructions:
        machine_code.append(instruction.to_machine_code())
            
    return machine_code

def write_to_file(file_name: str, machine_code: list[str]) -> None:
    with open(file_name, 'w') as f:
        for mcode in machine_code:
            f.write(mcode)
            f.write("\n")

lines = load_file_and_cleanup("rect/RectL.asm")
lines = parse_label_symbols(lines)
lines = parse_variables_symbols(lines)
instructions = parse_instructions(lines)
machine_code = generate_hack_machine_code(instructions)

write_to_file("rect/RectL.hack", machine_code)

