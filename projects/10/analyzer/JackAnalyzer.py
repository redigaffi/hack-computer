import sys
import re
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
import os
from pprint import pprint

def load_file(path):
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
   compilation_engine = CompilationEngine(tokenizer, file_name)

if __name__ == "__main__":
    path = sys.argv[1]

    # print("FILES BEFORE COMP:")
    # print(os.listdir(path))

    if os.path.isdir(path):
        print("DIR")
        print(path)
        files = os.listdir(path)
        for file in files:

            data = file.split(".")
            if data[-1] != "jack":
                continue

            name, extension = file.split(".")
            print(f"{path}/{file}", f"{path}/{name}.xml")
            compile_file(f"{path}/{file}", f"{path}/{name}.xml")
    else:
        print("FILE")
        print(path)
        data = path.split(".")
        compile_file(f"{path}", path.replace("jack", "xml"))

    # print("OUTPUT:")
    # print(os.listdir(path))
    if path == "Square":
        for file in os.listdir(path):
            print(f"chmod {file}")
            os.chmod(f"{path}/{file}", 0o777)
