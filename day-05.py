def getCrates(input):
    crates = [[] for i in range(9)]
    for line in input[:8]:
        for i in range(1,len(line),4):
            if line[i].isalpha():
                crates[i//4].append(line[i])
    return crates

with open('inputs/day-05.txt') as file:
    input = file.read().split('\n')

moves = [y.split(' ') for y in input[10:]]
moves = [[int(x[1]), int(x[3]), int(x[5])] for x in moves]

# Part 1
crates = getCrates(input)
for move in moves:
    for n in range(move[0]):
        item = crates[move[1]-1].pop(0)
        crates[move[2]-1].insert(0, item)
print('Day 05 Part 1:', ''.join([c[0] for c in crates]))

# Part 2
crates = getCrates(input)
for move in moves:
    items = []
    for n in range(move[0]):
        items.insert(0, crates[move[1]-1].pop(0))
    for i in items:
        crates[move[2]-1].insert(0, i)
print('Day 05 Part 2:', ''.join([c[0] for c in crates]))

# One-line Solutions
print('Day 05 Part 1:', ''.join([c[0] for c in crates] if not (input := open('inputs/day-05.txt').read().split('\n')) or not (moves := [[int(x[1]), int(x[3]), int(x[5])] for x in [y.split(' ') for y in input[10:]]]) or not (crates := [[] for i in range(9)]) or not [crates[j//4].append(line[j]) for line in input[:8] for j in range(1,len(line),4) if line[j].isalpha()] or [crates[move[2]-1].insert(0, crates[move[1]-1].pop(0)) for move in moves for n in range(move[0])] else ''))
print('Day 05 Part 2:', ''.join([c[0] for c in crates] if not (input := open('inputs/day-05.txt').read().split('\n')) or not (moves := [[int(x[1]), int(x[3]), int(x[5])] for x in [y.split(' ') for y in input[10:]]]) or not (crates := [[] for i in range(9)]) or not [crates[j//4].append(line[j]) for line in input[:8] for j in range(1,len(line),4) if line[j].isalpha()] or [crates[move[2]-1].insert(0, item) for move in moves for item in reversed([crates[move[1]-1].pop(0) for n in range(move[0])])] else ''))
