with open('inputs/day-01.txt') as file:
    groups = file.read().split('\n\n')

groups = [group.split('\n') for group in groups]
totals = [sum([int(x) for x in g]) for g in groups]
totals.sort(reverse=True)

# Part 1
print('Day 01 Part 1:', totals[0])

# Part 2
print('Day 01 Part 2:', sum(totals[:3]))

# One-line Solutions
print('Day 01 Part 1:', max([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('inputs/day-01.txt').read().split('\n\n')]]))
print('Day 01 Part 2:', sum(sorted([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('inputs/day-01.txt').read().split('\n\n')]], reverse=True)[0:3]))
