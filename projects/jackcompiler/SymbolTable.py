from dataclasses import dataclass 
from typing import Any
from enum import Enum, EnumMeta

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
            return True
        except ValueError:
            return False

class BaseEnum(str, Enum, metaclass=MetaEnum):
    pass

class VarKind(BaseEnum):
    STATIC = "static"
    FIELD = "field"
    ARG = "arg"
    VAR = "var"

class VarType(BaseEnum):
    INT = "int"
    CHAR = "char"
    BOOL = "boolean"
    STRING = "string"
    ARRAY = "array"
    CLASS_IDENTIFIER = "class_identifier"

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}
        self.var_kind_count = {
            VarKind.STATIC: 0,
            VarKind.FIELD: 0,
            VarKind.ARG: 0,
            VarKind.VAR: 0,
        }
    
    def define(self, name: str, var_type: VarType, kind: VarKind) -> None:
        assert name not in self.symbol_table, f"Var {name} already declared"
        if self.symbol_table.get(name, None) is None:
            self.symbol_table[name] = {
                "name": name,
                "type": var_type,
                "kind": kind,
                "index": self.var_kind_count[kind]
            }
            self.var_kind_count[kind] += 1

    def var_count(self, kind: VarKind) -> int:
        return self.var_kind_count[kind]

    def kind_of(self, name: str) -> VarKind:
        return self.symbol_table[name]["kind"] if name in self.symbol_table else None
    
    def type_of(self, name: str) -> VarType:
        return self.symbol_table[name]["type"] if name in self.symbol_table else None

    def index_of(self, name: str) -> int:
        return self.symbol_table[name]["index"] if name in self.symbol_table else None
