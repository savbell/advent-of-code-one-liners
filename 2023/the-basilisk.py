'''
One-line Python solution for Advent of Code 2023 (https://adventofcode.com/2023/)
Written by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code, affectionately nicknamed the Basilisk.
           Current progress:
            Day | Pt1 | Pt2
           -----------------
             01 |  ✔  |  ✔
See README and explanation of solutions at https://github.com/savbell/advent-of-code-one-liners
'''

import re
import os

# Input files not included in repo per Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# To run the Basilisk, replace with the paths to your own input files
input_files = {
    1 : '2023/day-01.txt',
}

q = {}
for day, path in input_files.items():
    q[day] = open(path).read()


################################ THE BASILISK ################################
print('Day 01 Part 1:', sum([int(re.findall(r'\d', l)[0] + re.findall(r'\d', l)[-1]) for l in q[1].split('\n')]), '\nDay 01 Part 2:', sum([int(''.join([{'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}[d] if d.isalpha() else d for d in [digits[0], digits[-1]]])) for l in q[1].split('\n') for digits in [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)]]))
