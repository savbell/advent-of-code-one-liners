'''
2023 Advent of Code - Day 13 (https://adventofcode.com/2023/day/13)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import itertools as it

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-13.txt'

# To match the format of input files for the Basilisk.
q = { 13: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
maps = [[list(row) for row in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]

def find_reflection(map):
    for col in range(1, len(map[0])):
        spit = min(col, len(map[0])-col)
        reflection = 1
        for row in map:
            if row[col-spit:col] != row[col:col+spit][::-1]:
                reflection = 0
                break
        if reflection:
            return col

columns = 0
rows = 0
for m in maps:
    vertical = find_reflection(m)
    horizontal = find_reflection(list(zip(*m)))
    columns += vertical if vertical else 0
    rows += horizontal*100 if horizontal else 0
    
print('Day 13 Part 1:', columns+rows)

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 13 Part 1:',((f:=lambda m:(a:=0,[(s:=min(c,len(m[0])-c),n:=1,[(r[c-s:c]!=r[c:c+s][::-1]) and (n:=0) for r in it.takewhile(lambda _:n==1,m)]) and (n and (a:=c)) for c in range(1,len(m[0]))]) and a),([[list(r) for r in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]),x:=0,y:=0,[(v:=f(m),h:=f(list(zip(*m))),(v and (x:=x+v)),(h and (y:=y+h*100))) for m in [[list(r) for r in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]]) and x+y)


######################## PART 2: MULTI-LINE SOLUTION ##########################
maps = [[list(row) for row in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]

def find_one_off_reflection(map):
    for col in range(1, len(map[0])):
        split = min(col, len(map[0])-col)
        num_differences = 0
        for row in map:
            for l, r in zip(row[col-split:col], row[col:col+split][::-1]):
                if l != r:
                    num_differences += 1
            if num_differences > 1:
                break
        if num_differences == 1:
            return col

columns = 0
rows = 0
for m in maps:
    vertical = find_one_off_reflection(m)
    horizontal = find_one_off_reflection(list(zip(*m)))
    columns += vertical if vertical else 0
    rows += horizontal*100 if horizontal else 0

print('Day 13 Part 2:', columns+rows)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 13 Part 2:',((f:=lambda m:(a:=0,[(s:=min(c,len(m[0])-c),n:=0,[[(l!=r and (n:=n+1)) for l,r in zip(r[c-s:c],r[c:c+s][::-1])] for r in m if n<=1],(n==1 and (a:=c))) for c in range(1,len(m[0]))]) and a),([[list(r) for r in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]),x:=0,y:=0,[(v:=f(m),h:=f(list(zip(*m))),(v and (x:=x+v)),(h and (y:=y+h*100))) for m in [[list(r) for r in m] for m in [m.split('\n') for m in q[13].strip().split('\n\n')]]]) and x+y)