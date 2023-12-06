'''
2023 Advent of Code - Day 06 (https://adventofcode.com/2023/day/6)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re
from functools import reduce

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-06.txt'

# To match the format of input files for the Basilisk.
q = { 6: open(input_file).read() }


######################### PART 1: MULTI-LINE SOLUTION #########################
def solve(b, c):
    return [(b+((b**2)-(4*c))**0.5)/2, (b-((b**2)-(4*c))**0.5)/2]

def num_valid_holds(interval):
    num = 0
    if interval[0] < interval[1]:
        num = int(interval[1]) - int(interval[0])
    else:
        num = int(interval[0]) - int(interval[1])
    if interval[0] % 1 == 0:
        num -= 1
    return num

nums = [int(n) for n in re.findall(r'\d+', q[6])]
races = [[nums[i], nums[i+int(len(nums)/2)]] for i in range(int(len(nums)/2))]

total = 1
for r in races:
    total *= num_valid_holds(solve(r[0], r[1]))

print('Day 06 Part 1:',total)

# ########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 06 Part 1:',(so:=lambda b,c:[(b+((b**2)-(4*c))**0.5)/2,(b-((b**2)-(4*c))**0.5)/2]) and (h:=lambda i:int(i[1])-int(i[0]) if i[0]<i[1] else int(i[0])-int(i[1]) if i[0]%1!=0 else int(i[0])-int(i[1])-1) and (u:=[int(n) for n in re.findall(r'\d+',q[6])]) and reduce(lambda a,b:a*b,[h(so(r[0], r[1])) for r in [[u[i],u[i+int(len(u)/2)]] for i in range(int(len(u)/2))]]))


######################### PART 2: MULTI-LINE SOLUTION #########################
def solve(b, c):
    return [(b+((b**2)-(4*c))**0.5)/2, (b-((b**2)-(4*c))**0.5)/2]

def num_valid_holds(interval):
    num = 0
    if interval[0] < interval[1]:
        num = int(interval[1]) - int(interval[0])
    else:
        num = int(interval[0]) - int(interval[1])
    if interval[0] % 1 == 0:
        num -= 1
    return num

nums = [n for n in re.findall(r'\d+', q[6])]
race = [int(''.join([n for n in nums[:int(len(nums)/2)]])), int(''.join([n for n in nums[int(len(nums)/2):]]))]

print('Day 06 Part 2:',num_valid_holds(solve(race[0], race[1])))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 06 Part 2:',(so:=lambda b,c:[(b+((b**2)-(4*c))**0.5)/2,(b-((b**2)-(4*c))**0.5)/2]) and (h:=lambda i:int(i[1])-int(i[0]) if i[0]<i[1] else int(i[0])-int(i[1]) if i[0]%1!=0 else int(i[0])-int(i[1])-1) and (u:=[n for n in re.findall(r'\d+',q[6])]) and (r:=[int(''.join([u[i] for i in range(int(len(u)/2))])), int(''.join([u[i] for i in range(int(len(u)/2),len(u))]))]) and h(so(r[0], r[1])))