with open('inputs/day-14.txt') as file:
    rocks = file.read().split('\n')

rocks = [[list(map(int, z.split(','))) for z in y] for y in [x.split(' -> ') for x in rocks]]

def extendCaveX(cave, i):
    if len(cave) == 0:
        cave.extend(list(list()) for _ in range(i+1))
    elif len(cave) <= i:
        cave.extend([['.' for _ in range(len(cave[0]))] for _ in range(i-len(cave)+2)])

def extendCaveY(cave, j):
    if len(cave[0]) <= j:
        [c.extend(['.' for _ in range(j-len(c)+2)]) for c in cave]
        
def caveSetup():
    cave = []
    for row in rocks:
        for l, line in enumerate(row):
            if l != len(row)-1:
                extendCaveX(cave, max(line[0], row[l+1][0]))
                if line[0] == row[l+1][0]:
                    for a in range(min(line[1], row[l+1][1]), max(line[1], row[l+1][1])+1):
                        extendCaveY(cave, a)
                        cave[line[0]][a] = '#'
                else:
                    for b in range(min(line[0], row[l+1][0]), max(line[0], row[l+1][0])+1):
                        cave[b][line[1]] = '#'
    return cave

# Part 1
cave = caveSetup()
stopAll = 0
sandCount = 0
while not stopAll:
    curX, curY = 500, 0
    for _ in range(len(cave[0])):
        if curY+1 > len(cave[0])-1:
            stopAll = 1
            sandCount -= 1
        elif cave[curX][curY+1] == '.':
            curY += 1
        elif cave[curX-1][curY+1] == '.':
            curX -= 1
            curY += 1
        elif cave[curX+1][curY+1] == '.':
            curX += 1
            curY += 1
        else:
            break
    cave[curX][curY] = 'o'
    sandCount += 1
    if cave[500][0] == 'o':
        stopAll = 1

print('Day 14 Part 1:', sandCount)

# Part 2
cave = caveSetup()
cave = [['.' for _ in range(len(cave[0]))] for _ in range(len(cave[0])+1)] + cave + [['.' for _ in range(len(cave[0]))] for _ in range(len(cave[0])+1)]
[c.extend(['.', '#']) for c in cave]
stopAll = 0
sandCount = 0
while not stopAll:
    curX, curY = 500+len(cave[0]), 0
    for _ in range(len(cave[0])):
        if curY+1 >= len(cave[0]):
            break
        elif cave[curX][curY+1] == '.':
            curY += 1
        elif cave[curX-1][curY+1] == '.':
            curX -= 1
            curY += 1
        elif cave[curX+1][curY+1] == '.':
            curX += 1
            curY += 1
        else:
            break
    cave[curX][curY] = 'o'
    sandCount += 1
    if cave[500+len(cave[0])][0] == 'o':
        stopAll = 1

print('Day 14 Part 2:', sandCount)