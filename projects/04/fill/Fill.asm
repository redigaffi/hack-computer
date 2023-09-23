(MAIN)
	// if any key pressed
	@KBD
	D=M
	@ONSCREEN
	D;JGT

	// else
	@8192 
	D=A
	@CLEARSCREEN
	0;JMP

	@MAIN
	0;JMP

// Clear all screen pixels
(CLEARSCREEN)
	@SCREEN
	A=D+A
	M=0
	D=D-1
	@CLEARSCREEN
	D;JGE
	@MAIN
	0;JMP

// Flip all screen pixels on
(ONSCREEN)
	//Set RAM[0] to screen size 8K 
	@8192 
	D=A
	@0 
	M=D

	// Set counter (i) at RAM[1]
	@1
	M=0

	// Copy counter (i) at RAM[1] to register D
	(ONSCREENLOOP)
	@1
	D=M

	@SCREEN
	A=A+D
	M=!M

	// Increment counter at RAM[1]
	@1
	M=M+1

	// Decrement counter at RAM[0]
	@0
	M=M-1
	D=M

	@ONSCREENLOOP
	D;JGT

// Keep screen black while key pressed (dont re-do previous work)
(MAINLOOP)
	@KBD
	D=M
	@MAINLOOP
	D;JGT

// else: no key pressed jump to main
@MAIN
0;JMP

