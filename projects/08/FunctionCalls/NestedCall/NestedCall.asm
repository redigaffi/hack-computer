
@Sys.init
0;JMP
//function Sys.init 0
(Sys.init)

//push constant 4000
@4000
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
//push constant 5000
@5000
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
//call Sys.main 0
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

@Sys.main
0;JMP
(Sys$ret.0)
//pop temp 1
@6
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
//label LOOP
(LOOP)
//goto LOOP
@LOOP
0;JMP

//function Sys.main 5
(Sys.main)

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

// push 0
@0
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 4001
@4001
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
//push constant 5001
@5001
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
//push constant 200
@200
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//pop local 1

@1
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
//push constant 40
@40
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//pop local 2

@2
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
//push constant 6
@6
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//pop local 3

@3
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
//push constant 123
@123
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//call Sys.add12 1
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

@Sys.add12
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
//push local 2

@2
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
//push local 3

@3
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
//push local 4

@4
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
//function Sys.add12 0
(Sys.add12)

//push constant 4002
@4002
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
//push constant 5002
@5002
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
//push constant 12
@12
D=A
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
