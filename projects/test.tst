// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/StaticTest/StaticTest.tst

load BasicLoop.asm,

set RAM[0] 256,    // initializes the stack pointer
set RAM[1] 300,   // base address of the local segment
set RAM[2] 400,   // base address of the argument segment
set RAM[400] 3,

repeat 1000 {       // enough cycles to complete the execution
  ticktock;
}

