'''
2023 Advent of Code - Day 04 (https://adventofcode.com/2023/day/4)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-04.txt'

# To match the format of input files for the Basilisk.
q = { 4: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
nums = re.findall(r': +((?:\d+\s+)+)\| +((?:\d+\s*)+)', q[4])
nums = [(set(map(int, n[0].split())), set(map(int, n[1].split()))) for n in nums]
nums = [n[0].intersection(n[1]) for n in nums]
scores = [2 ** (len(n) - 1) if len(n) > 0 else 0 for n in nums]

print('Day 04 Part 1:', sum(scores))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 04 Part 1:',sum([2**(len(n)-1) if len(n)>0 else 0 for n in [n[0].intersection(n[1]) for n in [(set(map(int,n[0].split())),set(map(int,n[1].split()))) for n in re.findall(r': +((?:\d+\s+)+)\| +((?:\d+\s*)+)',q[4])]]]))


######################### PART 2: MULTI-LINE SOLUTION #########################
nums = re.findall(r'\d+: +((?:\d+\s+)+)\| +((?:\d+\s*)+)', q[4])
nums = [(set(map(int, n[0].split())), set(map(int, n[1].split()))) for n in nums]
nums = [[1, len(n[0].intersection(n[1]))] for n in nums]
total_cards = 0
for i, n in enumerate(nums):
    total_cards += n[0]
    for _ in range(n[0]):
        for j in range(1,n[1]+1):
            nums[i+j][0] += 1

print('Day 04 Part 2:', total_cards)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 04 Part 2:',((c:=[[1,len(n[0].intersection(n[1]))] for n in [(set(map(int,n[0].split())), set(map(int,n[1].split()))) for n in re.findall(r'\d+: +((?:\d+\s+)+)\| +((?:\d+\s*)+)',q[4])]]) and not (t:=0) and [(t:=t+n[0]) and [c.__setitem__(i+j,[c[i+j][0]+1,c[i+j][1]]) for _ in range(n[0]) for j in range(1,n[1]+1)] for i, n in enumerate(c)] and t))
