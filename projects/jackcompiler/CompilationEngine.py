from JackTokenizer import Token, JackTokenizer, TokenType, Keyword, Symbol
from typing import Optional, List
from SymbolTable import SymbolTable, VarKind
from VMWriter import VMWriter, Segment, Command
from pprint import pprint

class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer, vm_writer: VMWriter):
        self.current_class_name = None
        self.current_subroutine_name = None
        self.current_subroutine_type = None
        self.has_subroutine_return = False
        self.labels = []

        self.tokenizer: JackTokenizer = tokenizer
        self.current_token: Token = tokenizer.tokens[self.tokenizer.token_pointer]
        self.class_level_symbol_table: SymbolTable  = SymbolTable()
        self.method_level_symbol_table: SymbolTable  = SymbolTable()
        self.vm_writer: VMWriter = vm_writer

        # Start compiling class
        self.compile_class()
        
    def get_x_previous_token(self, x) -> Token:
        return self.tokenizer.tokens[self.tokenizer.token_pointer-x]

    def get_symbol_table_for_var(self, name: str) -> SymbolTable:
        if self.method_level_symbol_table is not None:
            typeof = self.method_level_symbol_table.type_of(name)
        if typeof is None:
            typeof = self.class_level_symbol_table.type_of(name)
            return self.class_level_symbol_table if typeof is not None else None
        elif typeof is not None:
            return self.method_level_symbol_table

    def _process_identifier(self, name: str, category: str, index: int, declaring: bool):
        if self.tokenizer.has_more_tokens():
            self.tokenizer.advance()
            self.current_token: Token = self.tokenizer.tokens[self.tokenizer.token_pointer]

    def _process(self, expected_token: List[str], identifier_info: list = None):
        found = None
        for tok in expected_token:
            if tok in TokenType:
                if tok == self.current_token.token_type:
                    found = tok
                    break
            elif tok == self.current_token.token:
                found = tok

        assert found is not None, f"Expected {', '.join(expected_token)} instead found {self.current_token.token} {self.current_token.token_type} "

        if self.tokenizer.has_more_tokens():
            self.tokenizer.advance()
            self.current_token: Token = self.tokenizer.tokens[self.tokenizer.token_pointer]

    def look_ahead_by(self, num: int) -> Token:
        return self.tokenizer.tokens[self.tokenizer.token_pointer+num];

    def get_new_label(self, suffix: Optional[str] = None) -> str:
        label = f"{self.current_class_name}${self.current_subroutine_name}.{len(self.labels)}"
        if suffix:
            label = label + suffix
        self.labels.append(label)
        return label

    def compile_term(self):
        if self.current_token.token_type == TokenType.IDENTIFIER and self.look_ahead_by(1).token == "[":
            var_name = self.get_x_previous_token(0).token
            sbt = self.get_symbol_table_for_var(var_name)
            var_kind, index = sbt.kind_of(var_name), sbt.index_of(var_name)
            mapping = {
                VarKind.ARG: Segment.ARGUMENT,
                VarKind.VAR: Segment.LOCAL,
                VarKind.FIELD: Segment.THIS,
                VarKind.STATIC: Segment.STATIC,
            }


            self.vm_writer.writePush(mapping.get(var_kind), index)
            self._process([TokenType.IDENTIFIER])
            self._process(["["])
            self.compile_expression()
            self._process(["]"])

            self.vm_writer.writeArithmetic(Command.ADD)
            self.vm_writer.writePop(Segment.POINTER, 1)
            self.vm_writer.writePush(Segment.THAT, 0)

        elif self.current_token.token_type == TokenType.IDENTIFIER and self.look_ahead_by(1).token in ["(", "."]:
            self.compile_subroutine_call()
        elif self.current_token.token == "(":
            self._process(["("])
            self.compile_expression()
            self._process([")"])
        elif self.current_token.token == "~":
            self._process(["~"])
            self.compile_term()
            self.vm_writer.writeArithmetic(Command.NOT)
        elif self.current_token.token == "-":
            self._process(["-"])
            self.compile_term()
            self.vm_writer.writeArithmetic(Command.NEG)
        elif self.current_token.token_type == TokenType.IDENTIFIER:
            var_name = self.get_x_previous_token(0).token
            sbt = self.get_symbol_table_for_var(var_name)
            self._process([TokenType.IDENTIFIER])
            mapping = {
                VarKind.ARG: Segment.ARGUMENT,
                VarKind.VAR: Segment.LOCAL,
                VarKind.FIELD: Segment.THIS,
                VarKind.STATIC: Segment.STATIC,
            }

            var_kind, index = sbt.kind_of(var_name), sbt.index_of(var_name)
            if var_kind in mapping:
                self.vm_writer.writePush(mapping.get(var_kind), index)

        elif self.current_token.token_type == TokenType.INT_CONST:
            self.vm_writer.writePush(Segment.CONSTANT, self.current_token.token)
            self._process([TokenType.INT_CONST])
        elif self.current_token.token_type == TokenType.KEYWORD:
            if self.current_token.token == Keyword.FALSE:
                self.vm_writer.writePush(Segment.CONSTANT, 0)
            elif self.current_token.token == Keyword.TRUE:
                self.vm_writer.writePush(Segment.CONSTANT, 0)
                self.vm_writer.writeArithmetic(Command.NOT)
            elif self.current_token.token == Keyword.THIS:
                self.vm_writer.writePush(Segment.POINTER, 0)
            elif self.current_token.token == Keyword.NULL:
                self.vm_writer.writePush(Segment.CONSTANT, 0)

            self._process([*[keyword for keyword in Keyword]])
        elif self.current_token.token_type == TokenType.STRING_CONST:
            str_length = len(self.current_token.token)
            self.vm_writer.writePush(Segment.CONSTANT, str_length)
            self.vm_writer.writeCall("String.new", 1)
            self.vm_writer.writePop(Segment.TEMP, 0)
            for char in self.current_token.token:
                self.vm_writer.writePush(Segment.TEMP, 0)
                self.vm_writer.writePush(Segment.CONSTANT, ord(char))
                self.vm_writer.writeCall("String.appendChar", 2)
            self._process([TokenType.STRING_CONST])

    def compile_expression(self):
        self.compile_term()
        symbol_command_mapping = {
            Symbol.PLUS: lambda: self.vm_writer.writeArithmetic(Command.ADD),
            Symbol.MINUS: lambda: self.vm_writer.writeArithmetic(Command.SUB),
            Symbol.ASTERISK: lambda: self.vm_writer.writeCall("Math.multiply", 2),
            Symbol.SLASH: lambda: self.vm_writer.writeCall("Math.divide", 2),
            Symbol.AMPERSAND: lambda: self.vm_writer.writeArithmetic(Command.AND),
            Symbol.PIPE: lambda: self.vm_writer.writeArithmetic(Command.OR),
            Symbol.LESS_THAN: lambda: self.vm_writer.writeArithmetic(Command.LT),
            Symbol.GREATER_THAN: lambda: self.vm_writer.writeArithmetic(Command.GT),
            Symbol.EQUALS: lambda: self.vm_writer.writeArithmetic(Command.EQ),
        }

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
            op = self.current_token.token
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
            symbol_command_mapping.get(op)()

    def compile_types_and_user_defined_types(self):
        available_types = ["int", "char", "boolean", "void"]
        if self.current_token.token not in available_types:
            var_name = self.get_x_previous_token(0).token
            # self._process_identifier(var_name, "class", -1, False)
            self._process([TokenType.IDENTIFIER])
            return
        self._process(available_types)

    def compile_class_var_dec(self):
        while self.current_token.token not in ["function", "constructor", "method"]:
            self._process(["static", "field"])
            self.compile_types_and_user_defined_types()
            var_name = self.get_x_previous_token(0).token
            var_type = self.get_x_previous_token(1).token
            var_kind = self.get_x_previous_token(2).token
            self.class_level_symbol_table.define(var_name, var_type, var_kind)
            index = self.get_symbol_table_for_var(var_name).index_of(var_name)
            self._process([TokenType.IDENTIFIER])
            # self._process_identifier(var_name, var_kind, index, True)

            if self.current_token.token == ",":
                while self.current_token.token != ";":
                    self._process([","])
                    var_name = self.get_x_previous_token(0).token
                    self.class_level_symbol_table.define(var_name, var_type, var_kind)
                    index = self.get_symbol_table_for_var(var_name).index_of(var_name)
                    # self._process_identifier(var_name, var_kind, index, True)
                    self._process([TokenType.IDENTIFIER])

            self._process([";"])

    def compile_var_decl(self):
        if self.current_token.token != "var":
            return
        while True:
            self._process(["var"])
            self.compile_types_and_user_defined_types()

            var_name = self.get_x_previous_token(0).token
            var_type = self.get_x_previous_token(1).token
            var_kind = self.get_x_previous_token(2).token
            self.method_level_symbol_table.define(var_name, var_type, var_kind)
            index = self.get_symbol_table_for_var(var_name).index_of(var_name)
            # self._process_identifier(var_name, var_kind, index, True)
            self._process([TokenType.IDENTIFIER])

            if self.current_token.token == ",":
                while self.current_token.token != ";":
                    self._process([","])
                    var_name = self.get_x_previous_token(0).token
                    self.method_level_symbol_table.define(var_name, var_type, var_kind)
                    index = self.get_symbol_table_for_var(var_name).index_of(var_name)
                    # self._process_identifier(var_name, var_kind, index, True)
                    self._process([TokenType.IDENTIFIER])

            self._process([";"])
            if self.current_token.token != "var":
                return


    def compile_let(self):
        self._process(["let"])

        var_name = self.get_x_previous_token(0).token
        sbt: SymbolTable = self.get_symbol_table_for_var(var_name)
        var_kind, index = sbt.kind_of(var_name), sbt.index_of(var_name)
        self._process([TokenType.IDENTIFIER])

        mapping = {
            VarKind.ARG: Segment.ARGUMENT,
            VarKind.VAR: Segment.LOCAL,
            VarKind.FIELD: Segment.THIS,
            VarKind.STATIC: Segment.STATIC,
        }

        # Array access
        is_array = False
        if self.current_token.token == "[":
            is_array = True 
            self.vm_writer.writePush(mapping.get(var_kind), index)
            self._process(["["])
            self.compile_expression()
            self._process(["]"])
            # self.vm_writer.writePush(Segment.TEMP, 0)
            self.vm_writer.writeArithmetic(Command.ADD)
            
        self._process([Symbol.EQUALS])
        self.compile_expression()
        self._process([Symbol.SEMICOLON])

        if is_array:
            self.vm_writer.writePop(Segment.TEMP, 0)
            self.vm_writer.writePop(Segment.POINTER, 1)
            self.vm_writer.writePush(Segment.TEMP, 0)
            self.vm_writer.writePop(Segment.THAT, 0)
            return

        if var_kind in mapping:
            self.vm_writer.writePop(mapping.get(var_kind), index)

    def compile_if(self):
        self._process([Keyword.IF])
        self._process([Symbol.LEFT_PARENTHESIS])
        self.compile_expression()
        self.vm_writer.writeArithmetic(Command.NOT)
        label_1 = self.get_new_label()
        self.vm_writer.writeIf(label_1)
        self._process([Symbol.RIGHT_PARENTHESIS])
        self._process([Symbol.LEFT_CURLY_BRACE])
        self.compile_statements()
        label_2 = self.get_new_label()
        self.vm_writer.writeGoto(label_2)
        self._process([Symbol.RIGHT_CURLY_BRACE])
        self.vm_writer.writeLabel(label_1)
        if self.current_token.token == Keyword.ELSE:
            self._process([Keyword.ELSE])
            self._process([Symbol.LEFT_CURLY_BRACE])
            self.compile_statements()
            self._process([Symbol.RIGHT_CURLY_BRACE])
        self.vm_writer.writeLabel(label_2)

    def compile_while(self):
        label_1 = self.get_new_label()
        label_2 = self.get_new_label()
        self._process([Keyword.WHILE])
        self._process([Symbol.LEFT_PARENTHESIS])
        self.vm_writer.writeLabel(label_1)
        self.compile_expression()
        self.vm_writer.writeArithmetic(Command.NOT)
        self.vm_writer.writeIf(label_2)
        self._process([Symbol.RIGHT_PARENTHESIS])
        self._process([Symbol.LEFT_CURLY_BRACE])
        self.compile_statements()
        self.vm_writer.writeGoto(label_1)
        self._process([Symbol.RIGHT_CURLY_BRACE])
        self.vm_writer.writeLabel(label_2)

    def compile_expression_list(self) -> int:
        expression_amount = 0
        while self.current_token.token != ")":
            expression_amount += 1
            self.compile_expression()
            if self.current_token.token == ",":
                self._process([","])

        return expression_amount

    def compile_subroutine_call(self):
        if self.look_ahead_by(1).token == "(":
            function_name = self.get_x_previous_token(0).token
            self._process([TokenType.IDENTIFIER])
            self._process([Symbol.LEFT_PARENTHESIS])
            self.vm_writer.writePush(Segment.POINTER, 0)
            param_amount = self.compile_expression_list()
            self._process([Symbol.RIGHT_PARENTHESIS])
            self.vm_writer.writeCall(f"{self.current_class_name}.{function_name}", param_amount+1)
        elif self.look_ahead_by(1).token == ".":
            class_name = self.get_x_previous_token(0).token
            sbt: SymbolTable = self.get_symbol_table_for_var(class_name)
            param_amount = 0
            if sbt is not None:
                param_amount = 1
                segment, index, class_name = sbt.kind_of(class_name), sbt.index_of(class_name), sbt.type_of(class_name)
                mapping = {
                    VarKind.ARG: Segment.ARGUMENT,
                    VarKind.VAR: Segment.LOCAL,
                    VarKind.FIELD: Segment.THIS,
                }
                self.vm_writer.writePush(mapping.get(segment), index)

            self._process([TokenType.IDENTIFIER])
            self._process([Symbol.PERIOD])
            method_name = self.get_x_previous_token(0).token
            self._process([TokenType.IDENTIFIER])
            self._process([Symbol.LEFT_PARENTHESIS])
            param_amount += self.compile_expression_list()
            self._process([Symbol.RIGHT_PARENTHESIS])
            self.vm_writer.writeCall(f"{class_name}.{method_name}", param_amount)
            # self.vm_writer.writePop(Segment.TEMP, 0)

    def compile_do(self):
        self._process([Keyword.DO])
        self.compile_subroutine_call()
        # Do statement ignore return value 
        self.vm_writer.writePop(Segment.TEMP, 0)
        self._process([Symbol.SEMICOLON])

    def compile_return(self):
        self._process([Keyword.RETURN])
        has_return_value = False
        if self.current_token.token != Symbol.SEMICOLON:
            has_return_value = True 
            self.compile_expression()
        self._process([Symbol.SEMICOLON])

        if not has_return_value:
            self.vm_writer.writePush(Segment.CONSTANT, 0)

        self.vm_writer.writeReturn()

    def compile_statements(self):
        call_map = {
            Keyword.LET: self.compile_let,
            Keyword.IF: self.compile_if,
            Keyword.WHILE: self.compile_while,
            Keyword.DO: self.compile_do,
            Keyword.RETURN: self.compile_return,
        }

        while self.current_token.token in call_map:
            if self.current_token.token == Keyword.RETURN:
                self.has_subroutine_return = True

            call_map[self.current_token.token]()


    def compile_subroutine_body(self, func_name: str):
        self._process(["{"])
        self.compile_var_decl()

        self.vm_writer.writeFunction(f"{self.current_class_name}.{func_name}", self.method_level_symbol_table.var_count(VarKind.VAR))
        if self.current_subroutine_type == "constructor":
            # Find a block of memory with enough space to hold current object
            field_var_count = self.class_level_symbol_table.var_count(VarKind.FIELD)
            self.vm_writer.writePush(Segment.CONSTANT, field_var_count)
            self.vm_writer.writeCall("Memory.alloc", 1)
            self.vm_writer.writePop(Segment.POINTER, 0)
        elif self.current_subroutine_type == "method":
            # Set current object (this)
            self.vm_writer.writePush(Segment.ARGUMENT, 0)
            self.vm_writer.writePop(Segment.POINTER, 0)

        self.compile_statements()
        self._process(["}"])
        assert self.has_subroutine_return, "Subroutine has no return statement"

    def compile_subroutine_dec(self):
        while self.current_token.token in ["function", "constructor", "method"]:
            self.current_subroutine_type = self.current_token.token
            subroutine_type = self.current_token.token

            # Reset method level symbol table and push instance reference
            self.method_level_symbol_table = SymbolTable()

            if self.current_token.token == "method":
                self.method_level_symbol_table.define("this", self.current_class_name, "arg")

            self._process(["function", "constructor", "method"])
            self.compile_types_and_user_defined_types()

            func_name = self.get_x_previous_token(0).token
            func_type = self.get_x_previous_token(1).token

            self.current_subroutine_name = func_name
            self.has_subroutine_return = False
            self._process([TokenType.IDENTIFIER])
            self._process(["("])

            if self.current_token.token != ")":
                    while self.current_token.token != ")":
                        self.compile_types_and_user_defined_types()
                        var_name = self.get_x_previous_token(0).token
                        var_type = self.get_x_previous_token(1).token
                        self.method_level_symbol_table.define(var_name, var_type, "arg")
                        index = self.get_symbol_table_for_var(var_name).index_of(var_name)
                        # self._process_identifier(var_name, "arg", index, True)
                        self._process([TokenType.IDENTIFIER])

                        if self.current_token.token != ")":
                            self._process([","])
            self._process([")"])

            self.compile_subroutine_body(func_name)

    def compile_class(self):
        self._process(["class"])

        self.current_class_name = self.get_x_previous_token(0).token
        self._process([TokenType.IDENTIFIER])

        self._process(["{"])
        self.compile_class_var_dec()
        self.compile_subroutine_dec()
        self._process("}")

