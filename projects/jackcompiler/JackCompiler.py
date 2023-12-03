import sys
import re
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
from VMWriter import VMWriter
import os

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

def compile_file(input, file_name):
    data = load_file(input)
    tokenizer = JackTokenizer(data)
    with open(f"{file_name}.vm", "w+") as f:
        vm_writer = VMWriter(f)
        compilation_engine = CompilationEngine(tokenizer, vm_writer)

if __name__ == "__main__":
    path = sys.argv[1]
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            name, extension = file.split(".")
            if extension != "jack":
                continue

            compile_file(f"{path}/{file}", f"{path}/{name}")
    else:
        name, extension = path.split(".")
        compile_file(path, name)
