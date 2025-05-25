# Elementary Cellular Automata

This program simulates one-dimensional cellular automata. Each cell can either be 1 (alive) or 0 (dead). The next iteration of a cell is dependent on the value of the cell and its direct neighbors. Since these 3 values (left, cell, right) determine the next state, and each cell can be either 1 or 0, there are $2^3 = 8$ possible configurations. For every configuration, the evolved cell can be set to be either 0 or 1, like so:

![image](https://github.com/user-attachments/assets/42f67100-d41e-44b9-b200-043e06a6e19b)

This configuration is called Rule 30 because when the three cells are ordered by their binary equivalent (001 = 1, 010 = 2, 011 = 3), the corresponding new cells represent an 8-bit binary number. In this case, the configuration is 00011110 = 30. This also means there are $2^8 = 256$ elementary cellular automata. This program lets you explore each one by computing the result of any given rule (0-256).

# Sample Runs

![image](https://github.com/user-attachments/assets/ce6facf8-8b21-49cb-8640-62da3245cc6f)
![image](https://github.com/user-attachments/assets/08d01785-3139-426e-ac95-9b54bb59907e)
![image](https://github.com/user-attachments/assets/c45b983a-3707-4dad-934d-4a6a3fe36351)
![image](https://github.com/user-attachments/assets/1374de55-4304-4ffd-89b9-f51d408ec26a)


Reference:

Weisstein, Eric W. "Elementary Cellular Automaton." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
