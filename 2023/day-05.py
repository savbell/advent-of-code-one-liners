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
q = { 5: open(input_file).read().strip() }


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

def seed_to_location(index):
    return convert(convert(convert(convert(convert(convert(convert(index, soil), fertilizer), water), light), temperature), humidity), location)

locs = [seed_to_location(s) for s in seeds]

print('Day 05 Part 1:',min(locs))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 05 Part 1:',(v:=[[list(map(int,l.split())) for l in d.split('\n')] for d in [d for _,d in [re.split(r':\n',s) for s in re.split(r'\n\n',q[5].strip())[1:]]]]) and (c:=lambda i,m:(lambda c:c[0]+(i-c[1]) if c[1]+c[2]>i else i)(min([y for y in m if y[1]<=i],default=[0,0,0],key=lambda x:i-x[1]))) and min([c(s,v[6])for s in [c(s,v[5]) for s in [c(s,v[4]) for s in [c(s,v[3]) for s in [c(s,v[2]) for s in [c(s,v[1]) for s in [c(s,v[0]) for s in list(map(int,re.split(r'\n\n',q[5].strip())[0].split()[1:]))]]]]]]]))


######################### PART 2: MULTI-LINE SOLUTION #########################
########## Credit to Dylan Gray for his help with this solution!! #############
####################### https://github.com/DylanDmitri ########################
sections = re.split(r'\n\n', q[5].strip())
seeds = list(map(int, sections[0].split()[1:]))
maps = sections[1:]

current = [(a,a+b) for a,b in zip(seeds[::2], seeds[1::2])]

for table in maps:
    rows = [tuple(map(int, row.split())) for row in table.split('\n')[1:]]
    i_start = [-99]
    offsets = [0]
    latest_end = -99
    for row in sorted(rows, key=lambda row: row[1]):
        latest_end = max(latest_end, row[1]+row[2])
        offset = row[0] - row[1]
        if i_start and i_start[-1] == row[1]:
            i_start[-1] = row[1]
            offsets[-1] = offset
        else:
            i_start.append(row[1])
            offsets.append(offset)
        i_start.append(row[1]+row[2])
        offsets.append(0)

    out = []
    
    for interval in current:
        splits = [interval[0]]
        start_index = None
        for idx, post in enumerate(i_start):
            if post <= splits[-1]:
                continue
            if start_index is None:
                start_index = idx - 1
            if post < interval[1]:
                if post != interval[1]:
                    splits.append(post)
            else:
                break
        splits.append(interval[1])
        start_index = start_index or len(offsets)
        for a,b in zip(splits, splits[1:]):
            dx = offsets[min(start_index or float('inf'), len(offsets)-1)]
            start_index += 1
            out.append((a+dx, b+dx))
        
    current = out
    
print('Day 05 Part 2:',min(c[0] for c in current))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 05 Part 2:',[(v:=re.split(r'\n\n',q[5].strip())) and (s:=list(map(int,v[0].split()[1:]))) and (m:=v[1:]) and (c:=[(a,a+b) for a,b in zip(s[::2],s[1::2])]) and [[(w:=[tuple(map(int,x.split())) for x in g.split('\n')[1:]]) and (u:=[-99]) and (o:=[0]) and (l:=-99) and [(l:=max(l,(p:=r[0] - r[1])+r[1]+r[2])) and [(not u.__setitem__(-1,r[1]) and not o.__setitem__(-1,p)) if u and u[-1]==r[1] else (u.__iadd__([r[1]])) and o.__iadd__([p])] and (u.__iadd__([r[1]+r[2]]) and o.__iadd__([0])) for r in sorted(w,key=lambda x: x[1])] and not (t:=[]) and [(j:=[i[0]]) and not (h:=None) and [(((h:=d-1) if h is None else 0) and (j.__iadd__([p]) if p < i[1] and p != i[1] else 0) if not p <= j[-1] else 0) for d,p in enumerate(u)] and (j.__iadd__([i[1]]) and (h:=h or len(o))) and [(d:=o[min(h or float('inf'),len(o)-1)]) and (h:=h+1) and t.__iadd__([(a+d,b+d)]) for a,b in zip(j,j[1:])] for i in c]] and (c:=t) for g in m]] and min(x[0] for x in c))
