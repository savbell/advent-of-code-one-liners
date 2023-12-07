'''
2023 Advent of Code - Day 07 (https://adventofcode.com/2023/day/7)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

from itertools import groupby

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-07.txt'

# To match the format of input files for the Basilisk.
q = { 7: open(input_file).read() }


######################### PART 1: MULTI-LINE SOLUTION #########################
groups = [x.split() for x in q[7].split('\n')]
for g in groups:
    g[0] = ['AKQJT98765432'.index(c) + 1 for c in g[0]]

def score(h):
    s = sorted(h)
    if len(set(s)) == 1:
        return 7
    elif s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

for g in groups:
    g.append(score(g[0]))

groups.sort(key=lambda x: x[2])
ranked_groups = [list(g) for _, g in groupby(groups, lambda x: x[2])]
for g in ranked_groups:
    g.sort(key=lambda x: x[0], reverse=True)

groups = []
for g in ranked_groups:
    groups += g

total = 0
for i, g in enumerate(groups):
    total += int(g[1]) * (i+1)

print('Day 07 Part 1:',total)

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 07 Part 1:',(y:=[[['AKQJT98765432'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and [g.__iadd__([(s:=sorted(g[0])) and (7 if len(set(s))==1 else 6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in groupby(sorted(y,key=lambda x:x[2]), lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]))


######################## PART 2: MULTI-LINE SOLUTION ##########################
groups = [x.split() for x in q[7].split('\n')]
for g in groups:
    g[0] = ['AKQT98765432J'.index(c) + 1 for c in g[0]]

def score(h):
    if len(set(h)) == 1 or len(set(h)) == 2 and 13 in h:
        return 7
    replace = min([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 13])])
    s = sorted([replace if c == 13 else c for c in h])
    if s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

for g in groups:
    g.append(score(g[0]))

groups.sort(key=lambda x: x[2])
ranked_groups = [list(g) for _, g in groupby(groups, lambda x: x[2])]
for g in ranked_groups:
    g.sort(key=lambda x: x[0], reverse=True)

groups = []
for g in ranked_groups:
    groups += g

total = 0
for i, g in enumerate(groups):
    total += int(g[1]) * (i+1)

print('Day 07 Part 2:',total)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 07 Part 2:',(y:=[[['AKQT98765432J'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and (score:=lambda h:(7 if len(set(h)) == 1 or len(set(h)) == 2 and 13 in h else 0) or (s:=sorted([min([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 13])]) if c == 13 else c for c in h])) and (6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)) and [g.__iadd__([score(g[0])]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in groupby(sorted(y,key=lambda x:x[2]), lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]))