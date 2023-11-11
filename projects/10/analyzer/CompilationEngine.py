from JackTokenizer import Token, JackTokenizer, TokenType
from typing import Optional

class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer):
        self.tokenizer: JackTokenizer = tokenizer
        self.current_token: Token = tokenizer.tokens[self.tokenizer.token_pointer]
        self.compile_class()

    def _process(self, expected_token: Optional[str] = None, token_type: TokenType = None):
        if not expected_token and token_type == TokenType.IDENTIFIER:
            identifier = Token = self.tokenizer.tokens[self.tokenizer.token_pointer].token
            print(f"<identifier> {identifier} </identifier>")
        else:
            assert expected_token == self.current_token.token, f"Expected {token_type} {expected_token}, found {self.current_token}"
            print(f"<{token_type}> {expected_token} </{token_type}>")

        if self.tokenizer.has_more_tokens():
            self.tokenizer.advance()
            self.current_token: Token = self.tokenizer.tokens[self.tokenizer.token_pointer]

    def compilie_term(self):
        token_type = self.current_token.type
        if token_type == TokenType.IDENTIFIER:
            next_token = self.current_token[self.tokenizer.token_pointer+1]
            # Method call
            if next_token == ".":
                pass
            # Array access
            if next_token == "[":
                pass
            # Function calls
            if next_token == "(":
                pass

    def compile_class_var_dec(self):
        pass


    def compile_class(self):
        print("<class>")
        self._process("class", TokenType.KEYWORD)
        self._process(token_type=TokenType.IDENTIFIER)
        self._process("{", TokenType.SYMBOL)
        # self._process("}", TokenType.SYMBOL)
        print("</class>")

