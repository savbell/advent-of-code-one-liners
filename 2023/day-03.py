'''
2023 Advent of Code - Day 03 (https://adventofcode.com/2023/day/3)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-03.txt'

# To match the format of input files for the Basilisk.
q = { 3: open(input_file).read() }


######################### PART 1: MULTI-LINE SOLUTION #########################
num_coords = []
symbol_coords = []
for x, line in enumerate(q[3].split('\n')):
    nums = re.finditer(r'\d+', line)
    for n in nums:
        coords = []
        for i in range(len(n.group())):
            coords.append((x, n.start() + i))
        num_coords.append([n.group(), coords])
    symbols = re.finditer(r'[^.\d]', line)
    for s in symbols:
        symbol_coords.append([s.group(), (x, s.start())])
adj_nums = []
for n in num_coords:
    for c in n[1]:
        for s in symbol_coords:
            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                adj_nums.append(n) if n not in adj_nums else 0
                break
print('Day 03 Part 1:', sum([int(n[0]) for n in adj_nums]))
        

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 03 Part 1:',sum([int(n[0]) for n in [[n.group(),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] if any([abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1 for c in n[1] for s in [[s.group(),(x, s.start())] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[^.\d]',l)]])]))


######################### PART 2: MULTI-LINE SOLUTION #########################
num_coords = []
symbol_coords = []
for x, line in enumerate(q[3].split('\n')):
    nums = re.finditer(r'\d+', line)
    for n in nums:
        coords = []
        for i in range(len(n.group())):
            coords.append((x, n.start() + i))
        num_coords.append([int(n.group()), coords])
    symbols = re.finditer(r'[*]', line)
    for s in symbols:
        symbol_coords.append([s.group(), (x, s.start()), []])
for n in num_coords:
    for c in n[1]:
        for s in symbol_coords:
            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                s[2].append(n) if n not in s[2] else 0
                break

print('Day 03 Part 2:', sum([s[2][0][0] * s[2][1][0] for s in symbol_coords if len(s[2]) == 2]))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 03 Part 2:',(r:=[[s.group(),(x,s.start()),[]] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[*]',l)]) and [s[2].append(n) if n not in s[2] else 0 for n in [[int(n.group()),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] for c in n[1] for s in r if abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1] and sum([s[2][0][0]*s[2][1][0] for s in r if len(s[2])==2]))