
//push constant 10
@10
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop local 0

@0
D=A
@LCL
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


//push constant 21
@21
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 22
@22
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop argument 2

@2
D=A
@ARG
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


//pop argument 1

@1
D=A
@ARG
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


//push constant 36
@36
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop this 6

@6
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


//push constant 42
@42
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 45
@45
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop that 5

@5
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


//pop that 2

@2
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


//push constant 510
@510
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//pop temp 6

@11
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


//push local 0

@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push that 5

@5
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


//push argument 1

@1
D=A
@ARG
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


//push this 6

@6
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


//push this 6

@6
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


//push temp 6

@11
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

