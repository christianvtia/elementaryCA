import numpy as np
from matplotlib import pyplot

def check_rule(rule, state, position):
    left = state[position - 1]
    center = state[position]
    right = state[(position + 1) % len(state)]
    index = left * 4 + center * 2 + right
    return rule[index]

def run(initial_state, rule, iterations):
    evolution = [initial_state]
    for i in range(iterations):
        prev_state = evolution[i]
        next_state = np.zeros(len(initial_state), dtype=int)
        for j in range(len(initial_state)):
            next_state[j] = check_rule(rule, prev_state, j)
        evolution.append(next_state)
    return evolution
        
def plot_cellular_automata(evolution):
    pyplot.figure(figsize=(5,5))
    pyplot.imshow(evolution, cmap='gray')
    pyplot.show()

def decToBinary(n):
    binary_arr = np.zeros(8, dtype=int)
    i = 0
    while n >= 1:
        binary_arr[i] = n % 2
        n = n / 2
        i += 1
    return binary_arr

rule = int(input("Rule: "))
rule = decToBinary(rule)

num_iterations = 100
num_cells = 100


initial_state = np.zeros(num_cells, dtype=int)
initial_state[num_cells//2] = 1

evolution = run(initial_state, rule, num_iterations)
plot_cellular_automata(evolution)