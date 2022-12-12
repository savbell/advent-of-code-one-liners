with open('inputs/day-12.txt') as file:
    grid = file.read().split('\n')

grid = [[*l] for l in grid]

possibleStarts = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            grid[r][c] = 'a'
            start = (r, c)
        elif grid[r][c] == 'E':
            grid[r][c] = 'z'
            end = (r, c)
        if grid[r][c] == 'a':
            possibleStarts.append([((r, c), 0)])

def search(paths):
    visited = set()
    while len(paths) > 0:
        curPath = paths.pop(0)
        if curPath[0] == end:
            return curPath[1]
        elif curPath[0] not in visited:
            visited.add(curPath[0])
            for i in range(curPath[0][0]-1, curPath[0][0]+2):
                for j in range(curPath[0][1]-1, curPath[0][1]+2):
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i == curPath[0][0] or j == curPath[0][1]) \
                            and ((i, j) != curPath[0]) and ord(grid[i][j]) <= ord(grid[curPath[0][0]][curPath[0][1]])+1:
                        paths.append(((i, j), curPath[1]+1))

# Part 1
print('Day 12 Part 1:', search([(start, 0)]))

# Part 2
print('Day 12 Part 2:', min([n for n in [search([(s[0][0], 0)]) for s in possibleStarts] if n]))

# One-line Solutions coming soon!

