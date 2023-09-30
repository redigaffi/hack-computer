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
//call Sys.main 0
// push return address to stack
@test$ret.0
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
(test$ret.0)
//label LOOP
(LOOP)
//goto LOOP
@LOOP
0;JMP

//function Sys.main 0
(Sys.main)

//push constant 4000
@4000
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
