'''
2023 Advent of Code - Day 02 (https://adventofcode.com/2023/day/2)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-02.txt'

# To match the format of input files for the Basilisk.
q = { 2: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
games = re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)', q[2])
count = sum([int(g[0]) for g in games])
for g in games:
    dice = re.findall(r'(\d+)\s+(\w+)', g[1])
    for d in dice:
        n, c = int(d[0]), d[1]
        if (n > 12 and c == 'red') or (n > 13 and c == 'green') or (n > 14 and c == 'blue'):
            count -= int(g[0])
            break
print('Day 02 Part 1:', count)

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 02 Part 1:',sum([int(g[0]) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])])-sum([int(g[0]) for g in re.findall(r'Game (\d+):((?:\s*\d+\s+\w+,?;?)+)',q[2]) if any([int(d[0])>12 and d[1]=='red' or int(d[0])>13 and d[1]=='green' or int(d[0])>14 and d[1]=='blue' for d in re.findall(r'(\d+)\s+(\w+)',g[1])])]))


######################### PART 2: MULTI-LINE SOLUTION #########################
games = re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)', q[2])
power = 0
for g in games:
    dice = re.findall(r'(\d+)\s+(\w+)', g[1])
    t = {'red': [], 'green': [], 'blue': []}
    for d in dice:
        n, c = int(d[0]), d[1]
        t[c].append(int(n))
    power += max(t['red']) * max(t['green']) * max(t['blue'])
print('Day 02 Part 2:', power)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 02 Part 2:',sum([(m:=re.findall(r'(\d+)\s+(\w+)',g[1])) and max([int(d[0]) for d in m if d[1]=='red'])*max([int(d[0]) for d in m if d[1]=='green'])*max([int(d[0]) for d in m if d[1]=='blue']) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])]))
