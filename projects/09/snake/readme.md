Hello,

This is a typical snake game. You have a snake that you control with your arrow keys (up, down, left, right).
The snake needs to eat in order to grow, food will randomly appear on screen, the head needs to collide with 
the food in order to eat. The food will disappear in around 20s if you dont eat it, and appear in a new random place.

In order to start a game, the program will ask for some random characters, just write anything random, doesn't 
need to make sense. This is to generate some entropy in order to get psuedo-randomness, this makes each game unique.

If you hit the screen limits, you loose, also, if you hit your own body you loose.

I added comments on the comment where I thought it make sense.

Bugs I'm aware of:
- Screen flickering: not sure why it happens, is it a limitation of the virtual machine? can my code be further optimized?
- Sometimes food disappears before it's supposed and is placed in a new spot, might be a bug in the hit registry?

Thanks for reviewing and enjoy!
