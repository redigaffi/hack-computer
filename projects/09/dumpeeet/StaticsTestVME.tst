// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/08/FunctionCalls/StaticsTest/StaticsTestVME.tst

load,  // loads all the VM files from the current directory.
output-file Out.out,
output-list RAM[0]%D1.6.1;

repeat 6000000 {
  vmstep;
}

output;
