from pprint import pprint
from dataclasses import dataclass 
from typing import Any
from enum import StrEnum, EnumMeta

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
    @classmethod
    def max_length(cls):
        max_length = 0
        for const in cls:
            if len(const) > max_length:
                max_length = len(const) 
        return max_length

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

class TokenType(BaseEnum):
    KEYWORD = 'keyword'
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

    @staticmethod
    def get_char(index, data):
        try:
            return data[index]
        except:
            return None

    @staticmethod
    def is_symbol(char_pointer, data):
        char = JackTokenizer.get_char(char_pointer, data)
        if char in Symbol:
            return char_pointer+1, Token(TokenType.SYMBOL, char), True

        return char_pointer, None, False 

    @staticmethod
    def is_keyword(char_pointer, data):
        tmp = ""
        max_keyword_length = Keyword.max_length()

        i = 0
        # while tmp not in Keyword and len(tmp) < max_keyword_length:
        char = JackTokenizer.get_char(i+char_pointer, data)
        while char.isalpha() and len(tmp) < max_keyword_length:
            if not char:
                break
            tmp += char
            i += 1
            char = JackTokenizer.get_char(i+char_pointer, data)
            
        next_char = JackTokenizer.get_char(i+char_pointer+1, data)
        # if tmp in Keyword and next_char == " ":
        if tmp in Keyword:
            return char_pointer+i, Token(TokenType.KEYWORD, tmp), True

        return char_pointer, None, False 

    @staticmethod
    def is_string_const(char_pointer, data):
        tmp = ""

        # Starts with " 
        if data[char_pointer] != "\"":
            return char_pointer, None, False

        MAX_STRING = 128
        i = 1
        string_end = False
        while True:
            char = JackTokenizer.get_char(char_pointer+i, data) 
            if not char:
                break

            if char == "\"":
                string_end = True
                break

            tmp += char
            i += 1

        # Ends with "
        if string_end:
            return (char_pointer+i+1), Token(TokenType.STRING_CONST, tmp), True

        return char_pointer, None, False

    @staticmethod
    def is_int_const(char_pointer, data):
        tmp = ""

        MAX_INT_LENGTH = 5
        i = 0
        char = JackTokenizer.get_char(char_pointer+i, data)
        while char not in Symbol and i < MAX_INT_LENGTH :
            if not char:
                break
            tmp += char
            i += 1
            char = JackTokenizer.get_char(char_pointer+i, data)

        try:
            #TODO: Boundaries check
            num = int(tmp)
        except:
            return char_pointer, None, False

        return char_pointer+i, Token(TokenType.INT_CONST, int(tmp)), True

    @staticmethod
    def is_identifier(char_pointer, data):
        tmp = ""
        i = 0

        char = JackTokenizer.get_char(char_pointer+i, data)
        while char not in Symbol:
            if not char:
                break

            if char == " ":
                i += 1
                break

            tmp += data[char_pointer+i]
            i += 1

            char = JackTokenizer.get_char(char_pointer+i, data)

        return char_pointer+i, Token(TokenType.IDENTIFIER, tmp), True
        
    def __init__(self, data: str):
        self.tokens = []
        self.token_pointer = 0

        char_pointer = 0
        tokenizing_functions = [
            JackTokenizer.is_symbol,
            JackTokenizer.is_keyword,
            JackTokenizer.is_string_const,
            JackTokenizer.is_int_const,
            JackTokenizer.is_identifier
        ]

        length = len(data)
        while char_pointer < length:
            if JackTokenizer.get_char(char_pointer, data) == " ":
                char_pointer += 1
                continue

            for tokenizing_function in tokenizing_functions:
                result = tokenizing_function(char_pointer, data)
                if result[2]:
                    self.tokens.append(result[1])
                    char_pointer = result[0]
                    break

    def has_more_tokens(self) -> bool:
        return self.token_pointer < len(self.tokens)-1

    def advance(self):
        self.token_pointer += 1
        self.current_token = self.tokens[self.token_pointer]

    def token_type(self) -> TokenType:
        return self.tokens[self.token_pointer].token_type

    def keyword(self) -> Keyword:
        current_token = self.tokens[self.token_pointer]
        assert current_token in Keyword, "Current token not a keyword"
        return current_token

    def symbol(self):
        current_token = self.tokens[self.token_pointer]
        assert current_token in Symbol, "Current token not a symbol"
        return current_token

    def identifier(self) -> str:
        current_token = self.tokens[self.token_pointer]
        assert current_token.token_type == TokenType.IDENTIFIER, "Current token not a identifier"
        return current_token

    def int_val(self) -> int:
        current_token = self.tokens[self.token_pointer]
        assert current_token.token_type == TokenType.INT_CONST, "Current token not a int_const"
        return current_token

    def string_val(self) -> str:
        current_token = self.tokens[self.token_pointer]
        assert current_token.token_type == TokenType.STRING_CONST, "Current token not a string_const"
        return current_token

    def as_xml(self):
        output = """<tokens>\n"""
        for token in self.tokens:
            if token.token_type == TokenType.KEYWORD:
                output += f"""<keyword> {token.token} </keyword>\n"""
            elif token.token_type == TokenType.IDENTIFIER:
                output += f"""<identifier> {token.token} </identifier>\n"""
            elif token.token_type == TokenType.SYMBOL:
                replace = {
                    "<": "&lt;",
                    ">": "&gt;",
                    "&": "&amp;",
                }
                sym = token.token
                if token.token in replace:
                    sym = replace.get(token.token)
                output += f"""<symbol> {sym} </symbol>\n"""
            elif token.token_type == TokenType.INT_CONST:
                output += f"""<integerConstant> {token.token} </integerConstant>\n"""
            elif token.token_type == TokenType.STRING_CONST:
                output += f"""<stringConstant> {token.token} </stringConstant>\n"""

        output += """</tokens>"""
        return output
