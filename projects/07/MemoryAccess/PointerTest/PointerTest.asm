
//push constant 3030
@3030
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop pointer 0

@THIS
D=A
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
//SP--
@SP
M=M-1


//push constant 3040
@3040
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop pointer 1

@THAT
D=A
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
//SP--
@SP
M=M-1


//push constant 32
@32
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop this 2

@2
D=A
@THIS
A=D+M
D=A
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
//SP--
@SP
M=M-1


//push constant 46
@46
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop that 6

@6
D=A
@THAT
A=D+M
D=A
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
//SP--
@SP
M=M-1


//push pointer 0

@THIS
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push pointer 1

@THAT
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1


//add
@SP
A=M-1
D=M
A=A-1
D=M+D
@SP
A=M-1
A=A-1
M=D
//SP--
@SP
M=M-1


//push this 2

@2
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1


//sub
@SP
A=M-1
D=M
A=A-1
D=M-D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D
//SP--
@SP
M=M-1


//push that 6

@6
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1


//add
@SP
A=M-1
D=M
A=A-1
D=M+D
@SP
A=M-1
A=A-1
M=D
//SP--
@SP
M=M-1

