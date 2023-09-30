//push constant 0
@0
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
//label LOOP_START
(LOOP_START)
//push argument 0

@0
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
//push argument 0

@0
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
//push constant 1
@1
D=A
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
//pop argument 0

@0
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
//push argument 0

@0
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
//if-goto LOOP_START
//D = *SP
@SP
A=M-1
D=M

//SP--
@SP
M=M-1

// if D > 0 JUMP
@LOOP_START
D;JGT

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
