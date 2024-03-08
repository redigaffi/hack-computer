from io import TextIOWrapper
from enum import Enum, EnumMeta
from typing import Any

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
            return True
        except ValueError:
            return False

class BaseEnum(str, Enum, metaclass=MetaEnum):
    pass

class Segment(BaseEnum):
    CONSTANT = 'constant'
    ARGUMENT = 'argument'
    LOCAL = 'local'
    STATIC  = 'static'
    THIS = 'this'
    THAT = 'that'
    POINTER = 'pointer'
    TEMP = 'temp'
 
class Command(BaseEnum):
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
 
class VMWriter:
    def __init__(self, f: TextIOWrapper):
        self.output: TextIOWrapper = f

    def writePush(self, segment: Segment, index: int) -> None:
        self.output.write(f"push {segment} {index}\n")

    def writePop(self, segment: Segment, index: int) -> None:
        assert segment != Segment.CONSTANT, "Cant pop to constant segment"
        self.output.write(f"pop {segment} {index}\n")

    def writeArithmetic(self, command: Command) -> None:
        self.output.write(command + "\n")

    def writeLabel(self, label: str) -> None:
        self.output.write(f"label {label}\n")

    def writeGoto(self, label: str) -> None:
        self.output.write(f"goto {label}\n")
        
    def writeIf(self, label: str) -> None:
        self.output.write(f"if-goto {label}\n")

    def writeCall(self, name: str, nArgs: int) -> None:
        self.output.write(f"call {name} {nArgs}\n")

    def writeFunction(self, name: str, nVars: int) -> None:
        """
        Parameters:
        name (str): Function name
        nVars (int): Number of local vars the function has
        """
        self.output.write(f"function {name} {nVars}\n")

    def writeReturn(self) -> None:
        # How to handle in case of no return value?
        # push constant 0 as per function convention
        self.output.write("return\n")
