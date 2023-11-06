import sys
import re
from JackTokenizer import JackTokenizer

def load_file(path) -> list[str]:
    with open(path, "r") as hack_asm_file:
        lines = []
        for line in hack_asm_file:
            lines.append(line)

        return lines


if __name__ == "__main__":
    file = sys.argv[1]
    data = load_file(file)
    tokenizer = JackTokenizer(data)


