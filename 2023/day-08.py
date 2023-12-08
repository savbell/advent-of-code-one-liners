'''
2023 Advent of Code - Day 08 (https://adventofcode.com/2023/day/8)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import itertools as it
import math
import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-08.txt'

# To match the format of input files for the Basilisk.
q = { 8: open(input_file).read().strip() }

######################### PART 1: MULTI-LINE SOLUTION #########################
instructions = q[8].split('\n')[0]
nodes = [re.findall(r'(\w+) = \((\w+), (\w+)\)', line) for line in q[8].split('\n')[2:]]
first_node = nodes[0][0][0]
nodes = {node[0][0]: node[0][1:] for node in nodes}

cur = first_node
steps = 0
while not cur.endswith('Z'):
    for d in instructions:
        steps += 1
        if d == 'R':
            cur = nodes[cur][1]
        elif d == 'L':
            cur = nodes[cur][0]

print('Day 08 Part 1:',steps)


########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 08 Part 1:',(i:=q[8].split('\n')[0]) and (g:=[re.findall(r'(\w+) = \((\w+), (\w+)\)',l) for l in q[8].split('\n')[2:]]) and (g:=(u:=g[0][0][0]) and {o[0][0]:o[0][1:] for o in g}) and not (k:=0) and [((k:=k+1) and (u:=g[u][1] if d=='R' else g[u][0])) for d in it.takewhile(lambda _:(not u.endswith('Z')),it.cycle(i))] and k)


######################## PART 2: MULTI-LINE SOLUTION ##########################
instructions = q[8].split('\n')[0]
nodes = [re.findall(r'(\w+) = \((\w+), (\w+)\)', line) for line in q[8].split('\n')[2:]]
first_nodes = [n[0][0] for n in nodes if n[0][0].endswith('A')]
nodes = {n[0][0]: n[0][1:] for n in nodes}

all_steps = []
for node in first_nodes:
    cur = node
    steps = 0
    while not cur.endswith('Z'):
        for d in instructions:
            steps += 1
            if d == 'R':
                cur = nodes[cur][1]
            elif d == 'L':
                cur = nodes[cur][0]
    all_steps.append(steps)

# 13524038372771
print('Day 08 Part 2:',math.lcm(*all_steps))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 08 Part 2:',(i:=q[8].split('\n')[0]) and (g:=[re.findall(r'(\w+) = \((\w+), (\w+)\)', l) for l in q[8].split('\n')[2:]]) and (f:=[n[0][0] for n in g if n[0][0].endswith('A')]) and (g:={n[0][0]: n[0][1:] for n in g}) and not (a:=[]) and [(u:=o) and not (k:=0) and [((k:=k+1) and (u:=g[u][1] if d == 'R' else g[u][0])) for d in it.takewhile(lambda _:(not u.endswith('Z')),it.cycle(i))] and (a.__iadd__([k])) for o in f] and math.lcm(*a))