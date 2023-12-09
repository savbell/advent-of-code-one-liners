'''
2023 Advent of Code - Day 09 (https://adventofcode.com/2023/day/9)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
from functools import reduce
import itertools as it


input_file = '2023/day-09.txt'

# To match the format of input files for the Basilisk.
q = { 9: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
histories = [list(map(int,x.split())) for x in q[9].split('\n')]
final_nums = []
for h in histories:
    cur_nums = []
    while not all([x==0 for x in h]):
        cur_nums.append(h[-1])
        h = [h[i+1] - h[i] for i in range(len(h)-1)]
    final_nums.append(reduce(lambda x,y: x+y, cur_nums[::-1]))
    
print('Day 09 Part 1:',sum(final_nums))
    
########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 09 Part 1:',sum((h:=[list(map(int,x.split())) for x in q[9].split('\n')]) and not (p:=[]) and [not (b:=[]) and (c:=a.copy()) and [b.__iadd__([c[-1]]) and (c:=[c[i+1]-c[i] for i in range(len(c)-1)]) for _ in it.takewhile(lambda _:not all([x==0 for x in c]),it.repeat(None))] and p.__iadd__([reduce(lambda x,y:x+y,b[::-1])]) for a in h] and p))


######################## PART 2: MULTI-LINE SOLUTION ##########################
histories = [list(map(int,x.split())) for x in q[9].split('\n')]
final_nums = []
for h in histories:
    cur_nums = []
    while not all([x==0 for x in h]):
        cur_nums.append(h[0])
        h = [h[i+1] - h[i] for i in range(len(h)-1)]
    cur_nums.append(0)
    ending_num = 0
    for n in cur_nums[::-1]:
        ending_num = n - ending_num
    final_nums.append(ending_num)
    
print('Day 09 Part 2:',sum(final_nums))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 09 Part 2:',sum((h:=[list(map(int,x.split())) for x in q[9].split('\n')]) and not (p:=[]) and [not (b:=[]) and (c:=a.copy()) and [b.__iadd__([c[0]]) and (c:=[c[i+1]-c[i] for i in range(len(c)-1)]) for _ in it.takewhile(lambda _:not all([x==0 for x in c]),it.repeat(None))] and b.__iadd__([0]) and p.__iadd__(not (e:=0) and [e:=n-e for n in b[::-1]] and [e]) for a in h] and p))
