def getCrates(input):
    crates = [[] for i in range(9)]
    for line in input[:8]:
        for i in range(1,len(line),4):
            if line[i].isalpha():
                crates[i//4].append(line[i])
    return crates

with open('inputs/day-05.txt') as file:
    input = file.read().split('\n')

moves = [[int(x[1]), int(x[3]), int(x[5])] for x in [y.split(' ') for y in input[10:]]]

# Part 1
crates = getCrates(input)
for move in moves:
    for n in range(move[0]):
        item = crates[move[1]-1].pop(0)
        crates[move[2]-1].insert(0, item)
print(''.join([c[0] for c in crates]))

# Part 2
crates = getCrates(input)
for move in moves:
    items = []
    for n in range(move[0]):
        items.insert(0, crates[move[1]-1].pop(0))
    for i in items:
        crates[move[2]-1].insert(0, i)
print(''.join([c[0] for c in crates]))