'''
2023 Advent of Code - Day 12 (https://adventofcode.com/2023/day/12)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

from functools import cache
from itertools import product
import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-12.txt'

# To match the format of input files for the Basilisk.
q = { 12: open(input_file).read().strip() }

######################### PART 1: MULTI-LINE SOLUTION #########################
springs = [x.split() for x in q[12].strip().split('\n')]
springs = [[x[0], [int(y) for y in x[1].split(',')]] for x in springs]

def count_permutations(symbols):
    results = set()

    for symbol, counts in symbols:
        possibilities = []
        for s in symbol:
            if s == '?':
                possibilities.append(['#', '.'])
            else:
                possibilities.append([s])

        for combo in product(*possibilities):
            candidate = ''.join(combo)
            matches = re.findall(r'#+', candidate)
            match_lengths = [len(x) for x in matches]
            if match_lengths == counts:
                results.add(candidate)

    return len(results)

counts = [count_permutations([s]) for s in springs]

print('Day 12 Part 1:',sum(counts))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 12 Part 1:',sum([not (r:=set()) and [r.update([''.join(c) for c in product(*([['#','.'] if s=='?' else [s] for s in y])) if [len(x) for x in re.findall(r'#+',''.join(c))]==u]) for y,u in [s]] and len(r) for s in [[x[0],[int(y) for y in x[1].split(',')]] for x in [x.split() for x in q[12].strip().split('\n')]]]))


######################## PART 2: MULTI-LINE SOLUTION ##########################
########## Credit to Søren Fuglede Jørgensen for the their solution!! #########
######################## https://github.com/fuglede ###########################
springs = [x.split() for x in q[12].strip().split('\n')]
springs = [(x[0], tuple(map(int, x[1].split(',')))) for x in springs]
springs =[('?'.join([x[0]] * 5) + '.', x[1] * 5) for x in springs]

@cache
def count_permutations(symbols, counts, group_loc=0):
    if not symbols:
        return not counts and not group_loc
    results = 0
    possibilities = ['.', '#'] if symbols[0] == '?' else symbols[0]
    for p in possibilities:
        if p == '#':
            results += count_permutations(symbols[1:], counts, group_loc + 1)
        else:
            if group_loc > 0:
                if counts and counts[0] == group_loc:
                    results += count_permutations(symbols[1:], counts[1:])
            else:
                results = results + count_permutations(symbols[1:], counts)
    return results

counts = [count_permutations(s[0], s[1]) for s in springs]

print('Day 12 Part 2:',sum(counts))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 12 Part 2:',sum((count_permutations:=cache(lambda symbols, counts, group_loc=0: (not (results:=0) and [(results:=results+count_permutations(symbols[1:], counts, group_loc + 1)) if p == '#' else 1 and (group_loc > 0 and (counts and counts[0] == group_loc and (results:=results+count_permutations(symbols[1:], counts[1:])))) or (group_loc == 0 and (results:=results+count_permutations(symbols[1:], counts))) if p != '#' else 1 for p in (['.', '#'] if symbols[0] == '?' else symbols[0])] and results) if symbols else not counts and not group_loc)) and [count_permutations(s[0], s[1]) for s in [('?'.join([x[0]] * 5) + '.', x[1] * 5) for x in [(x[0], tuple(map(int, x[1].split(',')))) for x in [x.split() for x in q[12].strip().split('\n')]]]]))
