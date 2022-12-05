with open('inputs/day-01.txt') as file:
    groups = file.read().split('\n\n')

totals = [sum([int(x) for x in g]) for g in [group.split('\n') for group in groups]]
totals.sort(reverse=True)

# Part 1
print(totals[0])

# Part 2
print(sum(totals[:3]))