
// Bootstrap
// Set stack pointer
@256
D=A
@SP
M=D

// push return address to stack
@Bootstrap$ret.0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push LCL
@LCL
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push ARG
@ARG
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THIS 
@THIS
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THAT 
@THAT
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//ARG = SP-5-nArgs (no args)
@5
D=A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@Sys.init
0;JMP
(Bootstrap$ret.0)
//function Main.fibonacci 0
(Main.fibonacci)

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
//push constant 2
@2
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//lt
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D

// if D < 0 jump to GREATER
@JUMP_0
D;JLT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_0_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_0)
@SP
A=M-1
A=A-1
M=-1
(JUMP_0_END)

// SP--
@SP
M=M-1
//if-goto IF_TRUE
//D = *SP
@SP
A=M-1
D=M

//SP--
@SP
M=M-1

// if D != 0 JUMP
@IF_TRUE
D;JNE

//goto IF_FALSE
@IF_FALSE
0;JMP

//label IF_TRUE
(IF_TRUE)
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
//label IF_FALSE
(IF_FALSE)
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
//push constant 2
@2
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
//call Main.fibonacci 1
// push return address to stack
@Main$ret.0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push LCL
@LCL
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push ARG
@ARG
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THIS 
@THIS
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THAT 
@THAT
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//ARG = SP-5-nArgs
@1
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(Main$ret.0)
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
//call Main.fibonacci 1
// push return address to stack
@Main$ret.1
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push LCL
@LCL
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push ARG
@ARG
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THIS 
@THIS
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THAT 
@THAT
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//ARG = SP-5-nArgs
@1
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(Main$ret.1)
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
//function Sys.init 0
(Sys.init)

//push constant 4
@4
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//call Main.fibonacci 1
// push return address to stack
@Sys$ret.0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1


//push LCL
@LCL
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push ARG
@ARG
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THIS 
@THIS
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//push THAT 
@THAT
D=M

@SP
A=M
M=D
// SP++
@SP
M=M+1

//ARG = SP-5-nArgs
@1
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D

//LCL = SP
@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP
(Sys$ret.0)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP

