'''
2023 Advent of Code - Day 15 (https://adventofcode.com/2023/day/15)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-15.txt'

# To match the format of input files for the Basilisk.
q = { 15: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
steps = q[15].split(',')
values = []
for s in steps:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    values.append(value)

print('Day 15 Part 1:',sum(values))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 15 Part 1:',sum([(v:=0) or [v:=(v+ord(c))*17%256 for c in s] and v for s in q[15].split(',')]))


######################## PART 2: MULTI-LINE SOLUTION ##########################
steps = q[15].split(',')
boxes = [[] for _ in range(256)]
for s in steps:
    label = ''.join([c for c in s if c.isalpha()])
    operation = ''.join([c for c in s if not c.isalnum()])
    focal = ''.join([c for c in s if c.isdigit()])
    lens = (label, focal)
    box = 0
    for c in label:
        box += ord(c)
        box *= 17
        box %= 256
    if operation == '=':
        if label not in [x[0] for x in boxes[box]]:
            boxes[box].append(lens)
        else:
            index = [x[0] for x in boxes[box]].index(label)
            boxes[box].pop(index)
            boxes[box].insert(index, lens)
    elif operation == '-':
        if label in [x[0] for x in boxes[box]]:
            boxes[box].pop([x[0] for x in boxes[box]].index(label))

score = 0
for i,box in enumerate(boxes):
    for j,lens in enumerate(box):
        score += (i+1)*(j+1)*int(lens[1])
        
print('Day 15 Part 2:',score)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 15 Part 2:',sum((b:=[[] for _ in range(256)]) and [((l:=''.join([c for c in s if c.isalpha()])) and (o:=''.join([c for c in s if not c.isalnum()])) and (f:=''.join([c for c in s if c.isdigit()])) and (d:=(l,f)) and (a:=0) or 1) and not (a:=0) and [a:=(a+ord(c))*17%256 for c in l] and ((b[a].append(d) if l not in [x[0] for x in b[a]] else ((e:=[x[0] for x in b[a]].index(l)) or 1) and b[a].pop(e) and b[a].insert(e,d)) if o=='=' else b[a].pop([x[0] for x in b[a]].index(l)) if l in [x[0] for x in b[a]] else 0) for s in q[15].split(',')] and [(i+1)*(j+1)*int(n[1]) for i,p in enumerate(b) for j,n in enumerate(p)]))