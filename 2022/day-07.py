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
print('Day 07 Part 1:', sum(largeFiles))

# Part 2
spaceNeeded = dirs['//']-40000000
deletionCandidates = [x for x in dirs.values() if x > spaceNeeded]
print('Day 07 Part 2:', min(deletionCandidates))

# One-line Solutions
print('Day 07 Part 1:', sum([x for x in dirs.values() if x <= 100000] if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('inputs/day-07.txt').read().split('\n')]] else ''))
print('Day 07 Part 2:', min([x for x in dirs.values() if x > dirs['//']-40000000]) if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('inputs/day-07.txt').read().split('\n')]] else '')
