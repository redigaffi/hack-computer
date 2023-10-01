
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
//function Class1.set 0
(Class1.set)

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
//pop static 0
@Class1.0
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
//pop static 1
@Class1.1
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
//push constant 0
@0
D=A
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
//function Class1.get 0
(Class1.get)

//push static 0
@Class1.0
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1
//push static 1
@Class1.1
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
//function Class2.set 0
(Class2.set)

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
//pop static 0
@Class2.0
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
//pop static 1
@Class2.1
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
//push constant 0
@0
D=A
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
//function Class2.get 0
(Class2.get)

//push static 0
@Class2.0
D=M
@SP
A=M
M=D
// SP++
@SP
M=M+1
//push static 1
@Class2.1
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
//function Sys.init 0
(Sys.init)

//push constant 6
@6
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//push constant 8
@8
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//call Class1.set 2
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
@2
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

@Class1.set
0;JMP
(Sys$ret.0)
//pop temp 0
@5
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
//push constant 23
@23
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//push constant 15
@15
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//call Class2.set 2
// push return address to stack
@Sys$ret.1
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
@2
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

@Class2.set
0;JMP
(Sys$ret.1)
//pop temp 0
@5
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
//call Class1.get 0
// push return address to stack
@Sys$ret.2
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
@0
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

@Class1.get
0;JMP
(Sys$ret.2)
//call Class2.get 0
// push return address to stack
@Sys$ret.3
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
@0
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

@Class2.get
0;JMP
(Sys$ret.3)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP

