
//push constant 17
@17
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//eq
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-1] - STACK[SP-2]
D=D-M
@JUMP_0

// if D == 0 jump to EQUAL
D;JEQ

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


//push constant 17
@17
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 16
@16
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//eq
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-1] - STACK[SP-2]
D=D-M
@JUMP_1

// if D == 0 jump to EQUAL
D;JEQ

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_1_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_1)
@SP
A=M-1
A=A-1
M=-1
(JUMP_1_END)

// SP--
@SP
M=M-1


//push constant 16
@16
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//eq
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-1] - STACK[SP-2]
D=D-M
@JUMP_2

// if D == 0 jump to EQUAL
D;JEQ

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_2_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_2)
@SP
A=M-1
A=A-1
M=-1
(JUMP_2_END)

// SP--
@SP
M=M-1


//push constant 892
@892
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 891
@891
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
@JUMP_3
D;JLT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_3_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_3)
@SP
A=M-1
A=A-1
M=-1
(JUMP_3_END)

// SP--
@SP
M=M-1


//push constant 891
@891
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 892
@892
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
@JUMP_4
D;JLT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_4_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_4)
@SP
A=M-1
A=A-1
M=-1
(JUMP_4_END)

// SP--
@SP
M=M-1


//push constant 891
@891
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 891
@891
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
@JUMP_5
D;JLT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_5_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_5)
@SP
A=M-1
A=A-1
M=-1
(JUMP_5_END)

// SP--
@SP
M=M-1


//push constant 32767
@32767
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//gt
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D
@JUMP_6

// if D > 0 jump to GREATER
D;JGT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_6_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_6)
@SP
A=M-1
A=A-1
M=-1
(JUMP_6_END)

// SP--
@SP
M=M-1


//push constant 32766
@32766
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 32767
@32767
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//gt
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D
@JUMP_7

// if D > 0 jump to GREATER
D;JGT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_7_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_7)
@SP
A=M-1
A=A-1
M=-1
(JUMP_7_END)

// SP--
@SP
M=M-1


//push constant 32766
@32766
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//gt
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] - STACK[SP-1]
D=M-D
@JUMP_8

// if D > 0 jump to GREATER
D;JGT

// STACK[SP-2] = 0 (turn all bits off - false)
@SP
A=M-1
A=A-1
M=0
@JUMP_8_END
0;JMP

// STACK[SP-2] = -1 (turn all bits on - true)
(JUMP_8)
@SP
A=M-1
A=A-1
M=-1
(JUMP_8_END)

// SP--
@SP
M=M-1


//push constant 57
@57
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 31
@31
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//push constant 53
@53
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


//push constant 112
@112
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


//neg
@SP
A=M-1
D=!M
D=D+1
// STACK[SP-1] = D
@SP
A=M-1
M=D


//and
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] & STACK[SP-1]
D=M&D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D

// SP--
@SP
M=M-1


//push constant 82
@82
D=A
@SP
A=M
M=D
// SP++
@SP
M=M+1

//or
@SP
A=M-1
D=M
A=A-1

// D = STACK[SP-2] | STACK[SP-1]
D=M|D

// STACK[SP-2] = D
@SP
A=M-1
A=A-1
M=D

// SP--
@SP
M=M-1


//not
@SP
A=M-1
M=!M

