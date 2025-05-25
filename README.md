# Elementary Cellular Automata

This program simulates one-dimensional cellular automata. Each cell can either be 1 (alive) or 0 (dead). The next iteration of a cell is dependent on the value of the cell and its direct neighbors. Since these 3 values (left, cell, right) determine the next state, and each cell can be either 1 or 0, there are $2^3 = 8$ possible configurations. For every configuration, the evolved cell can be set to be either 0 or 1, like so:

![image](https://github.com/user-attachments/assets/42f67100-d41e-44b9-b200-043e06a6e19b)

This configuration is called Rule 30 because when the three cells are ordered by their binary equivalent (001 = 1, 010 = 2, 011 = 3), the corresponding new cells represent an 8-bit binary number. In this case, the configuration is 00011110 = 30. This also means there are $2^8 = 256$ elementary cellular automata. This program lets you explore each one by computing the result of any given rule (0-256).

# Sample Runs

![image](https://github.com/user-attachments/assets/3095d71f-e9c4-4232-9f29-bb4c8cd62e3f)
![image](https://github.com/user-attachments/assets/f5a2f601-0846-4828-ac61-e7b3f0e5b8f7)
![image](https://github.com/user-attachments/assets/5ec27007-7013-4d16-888f-2ceddeaa7a2b)
![image](https://github.com/user-attachments/assets/46624a84-3559-4063-81c4-c48f260bf038)



Reference:

Weisstein, Eric W. "Elementary Cellular Automaton." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
