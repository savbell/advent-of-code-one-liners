with open('inputs/day-04.txt') as file:
    assignments = file.read().split('\n')

sections = [x.split(',') for x in assignments]
sections = [[[int(x) for x in a.split('-')], [int(y) for y in b.split('-')]] for a, b in sections]

# Part 1
subsets = [(x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) for x in sections]
print('Day 04 Part 1:', sum(subsets))

# Part 2
overlaps = [x[0][0] <= x[1][1] and x[0][1] >= x[1][0] for x in sections]
print('Day 04 Part 2:', sum(overlaps))

# One-line Solutions
print('Day 04 Part 1:', sum([(n[0][0] >= n[1][0] and n[0][1] <= n[1][1]) or (n[0][0] <= n[1][0] and n[0][1] >= n[1][1]) for n in [[[int(x) for x in a.split('-')], [int(y) for y in b.split('-')]] for a, b in [x.split(',') for x in open('inputs/day-04.txt').read().split('\n')]]]))
print('Day 04 Part 2:', sum([n[0][0] <= n[1][1] and n[0][1] >= n[1][0] for n in [[[int(x) for x in a.split('-')], [int(y) for y in b.split('-')]] for a, b in [x.split(',') for x in open('inputs/day-04.txt').read().split('\n')]]]))
