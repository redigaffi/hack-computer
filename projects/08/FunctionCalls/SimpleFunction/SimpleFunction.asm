//function SimpleFunction.test 2
(SimpleFunction.test)

// push 0
@0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

// push 0
@0
D=A
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
//push local 1

@1
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
//not
@SP
A=M-1
M=!M
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
//return
// endFrame = LCL
@LCL
D=M
@endFrame
M=D

//retAddr = *(endFrame - 5)
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
M=D

//*ARG = pop
@SP
A=M-1
D=M
@ARG
A=M
M=D

// SP = ARG + 1 
@ARG
D=M+1
@SP
M=D

// THAT = *(endFrame - 1)
@1
D=A
@endFrame
D=M-D
A=D
D=M
@THAT
M=D

// THIS = *(endFrame - 2)
@2
D=A
@endFrame
D=M-D
A=D
D=M
@THIS
M=D

// ARG = *(endFrame - 3)
@3
D=A
@endFrame
D=M-D
A=D
D=M
@ARG
M=D

// LCL = *(endFrame - 4)
@4
D=A
@endFrame
D=M-D
A=D
D=M
@LCL
M=D

// goto retAddr
@retAddr
A=M
0;JMP
