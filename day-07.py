with open('inputs/day-07.txt') as file:
    commands = file.read().split('\n')

lines = [x.split(' ') for x in commands]
dirs = {}
curDirs = []
for l in lines:
    if l[0] == '$' and l[1] == 'cd':
        if l[2] == '/':
            curDirs = ['//']
            dirs['//'] = 0
        elif l[2] == '..':
            curDirs.pop()
        else:
            curDir = '/'.join(curDirs) + '/' + l[2]
            curDirs.append(curDir)
            if not dirs.get(curDir):
                dirs[curDir] = 0
    elif l[0].isdigit():
        for d in curDirs:
            dirs[d] += int(l[0])

# Part 1
largeFiles = [x for x in dirs.values() if x <= 100000]
print(sum(largeFiles))

# Part 2
spaceNeeded = dirs['//']-40000000
deletionCandidates = [x for x in dirs.values() if x > spaceNeeded]
print(min(deletionCandidates))