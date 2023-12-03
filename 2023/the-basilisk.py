'''
One-line Python solution for Advent of Code 2023 (https://adventofcode.com/2023/)
Written by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code, affectionately nicknamed the Basilisk.
           Current progress:
            Day | Pt1 | Pt2
           -----------------
             01 |  ✔  |  ✔
             02 |  ✔  |  ✔
             03 |  ✔  |  ✔
See README and explanation of solutions at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# To run the Basilisk, replace with the paths to your own input files
input_files = {
    1 : '2023/day-01.txt',
    2 : '2023/day-02.txt',
    3 : '2023/day-03.txt',
}

q = {}
for day, path in input_files.items():
    q[day] = open(path).read()


################################ THE BASILISK ################################
print('Day 01 Part 1:',sum([int(re.findall(r'\d',l)[0]+re.findall(r'\d',l)[-1]) for l in q[1].split('\n')]),'\nDay 01 Part 2:',sum([int(''.join([{'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}[d] if d.isalpha() else d for d in [n[0],n[-1]]])) for l in q[1].split('\n') for n in [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',l)]]),'\nDay 02 Part 1:',sum([int(g[0]) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])])-sum([int(g[0]) for g in re.findall(r'Game (\d+):((?:\s*\d+\s+\w+,?;?)+)',q[2]) if any([int(d[0])>12 and d[1]=='red' or int(d[0])>13 and d[1]=='green' or int(d[0])>14 and d[1]=='blue' for d in re.findall(r'(\d+)\s+(\w+)',g[1])])]),'\nDay 02 Part 2:',sum([max([int(d[0]) for d in re.findall(r'(\d+)\s+(\w+)',g[1]) if d[1]=='red'])*max([int(d[0]) for d in re.findall(r'(\d+)\s+(\w+)',g[1]) if d[1]=='green'])*max([int(d[0]) for d in re.findall(r'(\d+)\s+(\w+)',g[1]) if d[1]=='blue']) for g in re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)',q[2])]),'\nDay 03 Part 1:',sum([int(n[0]) for n in [[n.group(),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] if any([abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1 for c in n[1] for s in [[s.group(),(x, s.start())] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[^.\d]',l)]])]),'\nDay 03 Part 2:',(r:=[[s.group(),(x,s.start()),[]] for x,l in enumerate(q[3].split('\n')) for s in re.finditer(r'[*]',l)]) and [s[2].append(n) if n not in s[2] else 0 for n in [[int(n.group()),[(x,n.start()+i) for i in range(len(n.group()))]] for x,l in enumerate(q[3].split('\n')) for n in re.finditer(r'\d+',l)] for c in n[1] for s in r if abs(c[0]-s[1][0])<=1 and abs(c[1]-s[1][1])<=1] and sum([s[2][0][0]*s[2][1][0] for s in r if len(s[2])==2]))
