from enum import StrEnum, EnumMeta
from pprint import pprint
from dataclasses import dataclass 
from typing import Any

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
            return True
        except ValueError:
            return False

class BaseEnum(StrEnum, metaclass=MetaEnum):
    pass

class Keyword(BaseEnum):
    CLASS = 'class'
    CONSTRUCTOR = 'constructor'
    FUNCTION = 'function'
    METHOD = 'method'
    FIELD = 'field'
    STATIC = 'static'
    VAR = 'var'
    INT = 'int'
    CHAR = 'char'
    BOOLEAN = 'boolean'
    VOID = 'void'
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'
    THIS = 'this'
    LET = 'let'
    DO = 'do'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    RETURN = 'return'

class Symbol(BaseEnum):
    LEFT_CURLY_BRACE = '{'
    RIGHT_CURLY_BRACE = '}'
    LEFT_PARENTHESIS = '('
    RIGHT_PARENTHESIS = ')'
    LEFT_SQUARE_BRACKET = '['
    RIGHT_SQUARE_BRACKET = ']'
    PERIOD = '.'
    COMMA = ','
    SEMICOLON = ';'
    PLUS = '+'
    MINUS = '-'
    ASTERISK = '*'
    SLASH = '/'
    AMPERSAND = '&'
    PIPE = '|'
    LESS_THAN = '<'
    GREATER_THAN = '>'
    EQUALS = '='
    TILDE = '~'

class TokenType(StrEnum):
    KEYYWORD = 'keyword'
    SYMBOL = 'symbol'
    IDENTIFIER = 'identifier'
    INT_CONST = 'int_const'
    STRING_CONST = 'string_const'

@dataclass
class Token:
    token_type: TokenType
    token: Any

class JackTokenizer:
    token_pointer = 0
    tokens: list[Token] = []

    def __init__(self, data: str):
        for line in data:
            if line[:2] in ['//', '/*'] or line in ['\n', '\t', '\t\n']:
                continue

            token = ""
            for char in line:
                if char not in [" ", "\n", "\t"]:
                    token += char

                if token in Symbol:
                    tokens.append(Token(TokenType.SYMBOL, char))
                    token = ""
                    continue

                if token in Keyword:
                    tokens.append(Token(TokenType.KEYYWORD, token))
                    token = ""
                    continue


                tokens.append(Token(TokenType.IDENTIFIER, token))
                token = ""
                continue
                
                # print(token)
                # pprint(char)




    def has_more_tokens(self) -> bool:
        return False

    def advance(self):
        pass

    def token_type(self):
        pass

    def keyword(self):
        pass

    def symbol(self):
        pass

    def identifier(self) -> str:
        pass

    def int_val(self) -> int:
        pass

    def string_val(self) -> str:
        pass
