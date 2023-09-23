// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.


// zero result
@2
M=0

// Check if a is 0
@0
D=M
@21
D;JEQ

// Check if b is 0
@1
D=M
@21
D;JEQ

// Add b to M[3] a times
@1
D=M
@2
M=M+D
@1
D=M
@0
M=M-1
D=M
@2
D;JGT

