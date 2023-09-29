//label BEGGINING
(BEGGINING)

//push constant 1
@1
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1
//if-goto BEGGINING
//D = *SP
@SP
A=M-1
D=M
// if D > 0 JUMP
@BEGGINING
D;JGT

