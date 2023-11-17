from JackTokenizer import Token, JackTokenizer, TokenType, Keyword, Symbol
from typing import Optional, List
import xml.etree.ElementTree as ET

class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer):
        self.tokenizer: JackTokenizer = tokenizer
        self.current_token: Token = tokenizer.tokens[self.tokenizer.token_pointer]
        self.output = ""
        self.compile_class()

        element = ET.XML(self.output)
        ET.indent(element)
        with open("output.xml", "w") as f:
            f.write(str(ET.tostring(element, encoding='unicode', short_empty_elements=False)))

    def _process(self, expected_token: List[str]):
        found = None
        for tok in expected_token:
            if tok in TokenType:
                if tok == self.current_token.token_type:
                    found = tok
                    break
            elif tok == self.current_token.token:
                found = tok

        assert found is not None, f"Expected {', '.join(expected_token)} instead found {self.current_token.token} {self.current_token.token_type} "
        token_type = self.current_token.token_type

        xml_map = {
            TokenType.INT_CONST: "integerConstant",
            TokenType.STRING_CONST: "stringConstant"
        }
        value_map = {
            "<": "&lt;",
            ">": "&gt;",
            "&": "&amp;",
        }
        tag = xml_map[token_type] if token_type in xml_map else token_type
        value = value_map[self.current_token.token] if self.current_token.token in value_map else self.current_token.token
        self.output += f"<{tag}> {value} </{tag}>"

        if self.tokenizer.has_more_tokens():
            self.tokenizer.advance()
            self.current_token: Token = self.tokenizer.tokens[self.tokenizer.token_pointer]

    def look_ahead_by(self, num: int) -> Token:
        return self.tokenizer.tokens[self.tokenizer.token_pointer+num];

    def compile_term(self):
        self.output += "<term>"
        if self.current_token.token_type == TokenType.IDENTIFIER and self.look_ahead_by(1).token == "[":
            self._process([TokenType.IDENTIFIER])
            self._process(["["])
            self.compile_expression()
            self._process(["]"])
        elif self.current_token.token_type == TokenType.IDENTIFIER and self.look_ahead_by(1).token in ["(", "."]:
            self.compile_subroutine_call()
        elif self.current_token.token == "(":
            self._process(["("])
            self.compile_expression()
            self._process([")"])
        elif self.current_token.token in ["-", "~"]:
            self._process(["-", "~"])
            self.compile_term()
            # self._process([TokenType.INT_CONST,
            #            TokenType.STRING_CONST,
            #            TokenType.IDENTIFIER,
            #            *[keyword for keyword in Keyword]])
        else:
            self._process([TokenType.INT_CONST,
                           TokenType.STRING_CONST,
                           TokenType.IDENTIFIER,
                           *[keyword for keyword in Keyword]])
        self.output += "</term>"

    def compile_expression(self):
        self.output += "<expression>"
        self.compile_term()
        while self.current_token.token in [
                        Symbol.PLUS,
                        Symbol.MINUS,
                        Symbol.ASTERISK,
                        Symbol.SLASH,
                        Symbol.AMPERSAND,
                        Symbol.PIPE,
                        Symbol.LESS_THAN,
                        Symbol.GREATER_THAN,
                        Symbol.EQUALS,
                    ]:
            self._process([
                Symbol.PLUS,
                Symbol.MINUS,
                Symbol.ASTERISK,
                Symbol.SLASH,
                Symbol.AMPERSAND,
                Symbol.PIPE,
                Symbol.LESS_THAN,
                Symbol.GREATER_THAN,
                Symbol.EQUALS,
            ])
            self.compile_term()
        self.output += "</expression>"

    def compile_types_and_user_defined_types(self):
        available_types = ["int", "char", "boolean", "void"]
        if self.current_token.token not in available_types:
            self._process([TokenType.IDENTIFIER])
            return
        self._process(available_types)


    def compile_class_var_dec(self):
        while self.current_token.token not in ["function", "constructor", "method"]:
            self.output += "<classVarDec>"
            self._process(["static", "field"])
            self.compile_types_and_user_defined_types()
            self._process([TokenType.IDENTIFIER])
            if self.current_token.token == ",":
                while self.current_token.token != ";":
                    self._process([","])
                    self._process([TokenType.IDENTIFIER])

            self._process([";"])
            self.output += "</classVarDec>"

    def compile_var_decl(self):
        if self.current_token.token != "var":
            return
        while True:
            self.output += "<varDec>"
            self._process(["var"])
            self.compile_types_and_user_defined_types()
            self._process([TokenType.IDENTIFIER])
            if self.current_token.token == ",":
                while self.current_token.token != ";":
                    self._process([","])
                    self._process([TokenType.IDENTIFIER])

            self._process([";"])
            self.output += "</varDec>"
            if self.current_token.token != "var":
                return


    def compile_let(self):
        self.output += "<letStatement>"
        self._process(["let"])
        self._process([TokenType.IDENTIFIER])

        # Array access
        if self.current_token.token == "[":
            self._process(["["])
            self.compile_expression()
            self._process(["]"])

        self._process([Symbol.EQUALS])
        self.compile_expression()
        self._process([Symbol.SEMICOLON])
        self.output += "</letStatement>"

    def compile_if(self):
        self.output += "<ifStatement>"
        self._process([Keyword.IF])
        self._process([Symbol.LEFT_PARENTHESIS])
        self.compile_expression()
        self._process([Symbol.RIGHT_PARENTHESIS])
        self._process([Symbol.LEFT_CURLY_BRACE])
        self.compile_statements()
        self._process([Symbol.RIGHT_CURLY_BRACE])
        if self.current_token.token == Keyword.ELSE:
            self._process([Keyword.ELSE])
            self._process([Symbol.LEFT_CURLY_BRACE])
            self.compile_statements()
            self._process([Symbol.RIGHT_CURLY_BRACE])
        self.output += "</ifStatement>"

    def compile_while(self):
        self.output += "<whileStatement>"
        self._process([Keyword.WHILE])
        self._process([Symbol.LEFT_PARENTHESIS])
        self.compile_expression()
        self._process([Symbol.RIGHT_PARENTHESIS])
        self._process([Symbol.LEFT_CURLY_BRACE])
        self.compile_statements()
        self._process([Symbol.RIGHT_CURLY_BRACE])
        self.output += "</whileStatement>"

    def compile_expression_list(self):
        self.output += "<expressionList>"
        while self.current_token.token != ")":
            self.compile_expression()
            if self.current_token.token == ",":
                self._process([","])
        self.output += "\n</expressionList>"

    def compile_subroutine_call(self):
        self._process([TokenType.IDENTIFIER])
        if self.current_token.token == "(":
            self._process([Symbol.LEFT_PARENTHESIS])
            # if self.current_token.token != ")":
            self.compile_expression_list()
            self._process([Symbol.RIGHT_PARENTHESIS])

        elif self.current_token.token == ".":
            self._process([Symbol.PERIOD])
            self._process([TokenType.IDENTIFIER])
            self._process([Symbol.LEFT_PARENTHESIS])
            # if self.current_token.token != ")":
            self.compile_expression_list()
            self._process([Symbol.RIGHT_PARENTHESIS])

    def compile_do(self):
        self.output += "<doStatement>"
        self._process([Keyword.DO])
        self.compile_subroutine_call()
        self._process([Symbol.SEMICOLON])
        self.output += "</doStatement>"

    def compile_return(self):
        self.output += "<returnStatement>"
        self._process([Keyword.RETURN])
        if self.current_token.token != Symbol.SEMICOLON:
            self.compile_expression()
        self._process([Symbol.SEMICOLON])
        self.output += "</returnStatement>"

    def compile_statements(self):
        call_map = {
            Keyword.LET: self.compile_let,
            Keyword.IF: self.compile_if,
            Keyword.WHILE: self.compile_while,
            Keyword.DO: self.compile_do,
            Keyword.RETURN: self.compile_return,
        }

        self.output += "<statements>"
        while self.current_token.token in call_map:
            call_map[self.current_token.token]()
        self.output += "\n</statements>"


    def compile_subroutine_body(self):
        self.output += "<subroutineBody>"
        self._process(["{"])
        self.compile_var_decl()
        self.compile_statements()
        self._process(["}"])
        self.output += "</subroutineBody>"

    def compile_subroutine_dec(self):
        while self.current_token.token in ["function", "constructor", "method"]:
            self.output += "<subroutineDec>"
            self._process(["function", "constructor", "method"])
            self.compile_types_and_user_defined_types()
            self._process([TokenType.IDENTIFIER])

            self._process(["("])

            self.output += "<parameterList>\n"
            if self.current_token.token != ")":
                    while self.current_token.token != ")":
                        self.compile_types_and_user_defined_types()
                        self._process([TokenType.IDENTIFIER])

                        if self.current_token.token != ")":
                            self._process([","])

            self.output += "</parameterList>"

            self._process([")"])
            self.compile_subroutine_body()
            self.output += "</subroutineDec>"

    def compile_class(self):
        self.output += "<class>"
        self._process(["class"])
        self._process([TokenType.IDENTIFIER])
        self._process(["{"])
        self.compile_class_var_dec()
        self.compile_subroutine_dec()
        self._process("}")
        self.output += "</class>"

