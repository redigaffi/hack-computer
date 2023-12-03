import sys
import re
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
from VMWriter import VMWriter

def load_file(path) -> list[str]:
    data = ""
    with open(path, "r") as hack_asm_file:
        for line in hack_asm_file:
            if line == "\n" or line == "\t":
                continue
           
            removed_comments = re.sub("(\/\/.*)", "", line)
            cleaned = removed_comments.strip()

            for char in cleaned:
                data += char

        data = re.sub(r"/\*\*(.*?)\*/", "", data)
        return data

if __name__ == "__main__":
    file = sys.argv[1]
    data = load_file(file)
    tokenizer = JackTokenizer(data)
    with open("output.vm", "w+") as f:
        vm_writer = VMWriter(f)
        compilation_engine = CompilationEngine(tokenizer, vm_writer)

