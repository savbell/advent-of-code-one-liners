with open('inputs/day-08.txt') as file:
    t = file.read().split('\n')

t = [[int(y) for y in x] for x in t]

# Part 1
count = 0
for r in range(len(t)):
    for c in range(len(t[r])):
        treesLeft = [x for x in t[r][:c] if x >= t[r][c]]
        treesRight = [x for x in t[r][c+1:] if x >= t[r][c]]
        treesUp = [x[c] for i, x in enumerate(t) if x[c] >= t[r][c] and i < r]
        treesDown = [x[c] for i, x in enumerate(t) if x[c] >= t[r][c] and i > r]
        count += not (treesLeft and treesRight and treesUp and treesDown)
print('Day 08 Part 1:', count)

# Part 2
maxScore = 0
for r in range(len(t)):
    for c in range(len(t[r])):
        treesLeft = sum([(x < t[r][c]) or (found:=True) for x in t[r][:c][::-1] if not found] if not (found:=False) else '')
        treesRight = sum([(x < t[r][c]) or (found:=True) for x in t[r][c+1:] if not found] if not (found:=False) else '')
        treesUp = sum([(x[c] < t[r][c]) or (found:=True) for i, x in reversed(list(enumerate(t))) if not found and i < r] if not (found:=False) else '')
        treesDown = sum([(x[c] < t[r][c]) or (found:=True) for i, x in enumerate(t) if not found and i > r] if not (found:=False) else '')
        scenicScore = treesLeft * treesRight * treesUp * treesDown
        if scenicScore > maxScore:
            maxScore = scenicScore
print('Day 08 Part 2:', maxScore)

# One-line Solutions
print('Day 08 Part 1:', sum([not bool([x for x in t[r][:c] if x >= t[r][c]] and [x for x in t[r][c+1:] if x >= t[r][c]] and [x[c] for i, x in enumerate(t) if x[c] >= t[r][c] and i < r] and [x[c] for i, x in enumerate(t) if x[c] >= t[r][c] and i > r]) for t in [[[int(y) for y in x] for x in open('inputs/day-08.txt').read().split('\n')]] for r in range(len(t)) for c in range(len(t[r]))]))
print('Day 08 Part 2:', max([sum([(x < t[r][c]) or (found:=True) for x in t[r][:c][::-1] if not found] if not (found:=False) else '') * sum([(x < t[r][c]) or (found:=True) for x in t[r][c+1:] if not found] if not (found:=False) else '') * sum([(x[c] < t[r][c]) or (found:=True) for i, x in reversed(list(enumerate(t))) if not found and i < r] if not (found:=False) else '') * sum([(x[c] < t[r][c]) or (found:=True) for i, x in enumerate(t) if not found and i > r] if not (found:=False) else '') for t in [[[int(y) for y in x] for x in open('inputs/day-08.txt').read().split('\n')]] for r in range(len(t)) for c in range(len(t[r]))]))
