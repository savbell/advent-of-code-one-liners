'''
2023 Advent of Code - Day 05 (https://adventofcode.com/2023/day/5)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-05.txt'

# To match the format of input files for the Basilisk.
q = { 5: open(input_file).read() }


######################### PART 1: MULTI-LINE SOLUTION #########################
def convert(index, mapping):
    closest = min([y for y in mapping if y[1]<=index], default=[0,0,0], key=lambda x: index-x[1])
    if closest[1] + closest[2] > index:
        return closest[0] + (index - closest[1])
    return index

seeds = []
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []

sections = re.split(r'\n\n', q[5].strip())
seeds = list(map(int, sections[0].split()[1:]))
for section in sections[1:]:
    title, data = re.split(r':\n', section)
    data_list = [list(map(int, line.split())) for line in data.split('\n')]
    if '-soil' in title:
        soil = data_list
    elif '-fertilizer' in title:
        fertilizer = data_list
    elif '-water' in title:
        water = data_list
    elif '-light' in title:
        light = data_list
    elif '-temperature' in title:
        temperature = data_list
    elif '-humidity' in title:
        humidity = data_list
    elif '-location' in title:
        location = data_list

humidity_to_location = [convert(s, location) for s in [convert(s, humidity) for s in [convert(s, temperature) for s in [convert(s, light) for s in [convert(s, water) for s in [convert(s, fertilizer) for s in [convert(s, soil) for s in seeds]]]]]]]

print('Day 05 Part 1:',min(humidity_to_location))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 05 Part 1:',(v:=[[list(map(int,l.split())) for l in d.split('\n')] for d in [d for _,d in [re.split(r':\n',s) for s in re.split(r'\n\n',q[5].strip())[1:]]]]) and (c:=lambda i,m:(lambda c:c[0]+(i-c[1]) if c[1]+c[2]>i else i)(min([y for y in m if y[1]<=i],default=[0,0,0],key=lambda x:i-x[1]))) and min([c(s,v[6])for s in [c(s,v[5]) for s in [c(s,v[4]) for s in [c(s,v[3]) for s in [c(s,v[2]) for s in [c(s,v[1]) for s in [c(s,v[0]) for s in list(map(int,re.split(r'\n\n',q[5].strip())[0].split()[1:]))]]]]]]]))


######################### PART 2: MULTI-LINE SOLUTION #########################
# Haven't started yet...

########################## PART 2: ONE-LINE SOLUTION ##########################
# Haven't started yet...
