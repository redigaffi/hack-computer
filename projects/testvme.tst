// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

load BasicLoop.vm,
output-file BasicLoop.out,
output-list RAM[0]%D1.6.1 RAM[256]%D1.6.1;

set sp 256,
set local 300,
set argument 400,
set argument[0] 3,

repeat 33 {
  vmstep;
}

