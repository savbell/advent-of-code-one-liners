with open('./day-01.txt') as file:
    groups = file.read().split('\n\n')

totals = [sum([int(x) for x in g]) for g in [group.split('\n') for group in groups]]

biggest = []
for i in range(3):
    top = max(totals)
    biggest.append(top)
    totals.remove(top)

print(biggest, sum(biggest))