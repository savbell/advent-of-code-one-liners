'''
2023 Advent of Code - Day 01 (https://adventofcode.com/2023/day/1)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-01.txt'

# To match the format of input files for the Basilisk.
q = { 1: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
lines = q[1].split('\n')
calibration = 0
for l in lines:
    digits = re.findall(r'\d', l)
    calibration += int(digits[0] + digits[-1])

print('Day 01 Part 1:', calibration)

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 01 Part 1:',sum([(d:=re.findall(r'\d',l)) and int(d[0]+d[-1]) for l in q[1].split('\n')]))


######################### PART 2: MULTI-LINE SOLUTION #########################
lines = q[1].split('\n')

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

calibration = 0
for l in lines:
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)
    value = ''.join([numbers[d] if d.isalpha() else d for d in [digits[0], digits[-1]]])
    calibration += int(value)

print('Day 01 Part 2:', calibration)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 01 Part 2:',sum([int(''.join([{'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}[d] if d.isalpha() else d for d in [n[0], n[-1]]])) for l in q[1].split('\n') for n in [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)]]))
