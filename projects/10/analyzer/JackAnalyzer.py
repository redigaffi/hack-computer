import sys
import re
from JackTokenizer import JackTokenizer

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
    with open("output.xml", "w+") as f:
        f.write(tokenizer.as_xml())

