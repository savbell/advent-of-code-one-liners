# Day 01
print('Day 01 Part 1:', max([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('inputs/day-01.txt').read().split('\n\n')]]))
print('Day 01 Part 2:', sum(sorted([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('inputs/day-01.txt').read().split('\n\n')]], reverse=True)[0:3]))

# Day 02
print('Day 02 Part 1:', sum([{'A X':3+1,'A Y':6+2,'A Z':0+3,'B X':0+1,'B Y':3+2,'B Z':6+3,'C X':6+1,'C Y':0+2,'C Z':3+3}[x] for x in open('inputs/day-02.txt').read().split('\n')]))
print('Day 02 Part 2:', sum([{'A X':0+3,'A Y':3+1,'A Z':6+2,'B X':0+1,'B Y':3+2,'B Z':6+3,'C X':0+2,'C Y':3+3,'C Z':6+1}[x] for x in open('inputs/day-02.txt').read().split('\n')]))

# Day 03
print('Day 03 Part 1:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(x).intersection(y).pop() for x, y in [[i[:len(i)//2], i[len(i)//2:]] for i in open('inputs/day-03.txt').read().split('\n')]]]))
print('Day 03 Part 2:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(open('inputs/day-03.txt').read().split('\n')[i]).intersection(open('inputs/day-03.txt').read().split('\n')[i+1]).intersection(open('inputs/day-03.txt').read().split('\n')[i+2]).pop() for i in range(0,len(open('inputs/day-03.txt').read().split('\n')),3)]]))

# Day 04
print('Day 04 Part 1:', sum([(n[0][0] >= n[1][0] and n[0][1] <= n[1][1]) or (n[0][0] <= n[1][0] and n[0][1] >= n[1][1]) for n in [[[int(x) for x in a.split('-')], [int(y) for y in b.split('-')]] for a, b in [x.split(',') for x in open('inputs/day-04.txt').read().split('\n')]]]))
print('Day 04 Part 2:', sum([n[0][0] <= n[1][1] and n[0][1] >= n[1][0] for n in [[[int(x) for x in a.split('-')], [int(y) for y in b.split('-')]] for a, b in [x.split(',') for x in open('inputs/day-04.txt').read().split('\n')]]]))

# Day 05 - This one is a bit cheese but I'm doing my best. Requires Python 3.8 (https://peps.python.org/pep-0572/)
print('Day 05 Part 1:', ''.join([c[0] for c in crates] if not (input := open('inputs/day-05.txt').read().split('\n')) or not (moves := [[int(x[1]), int(x[3]), int(x[5])] for x in [y.split(' ') for y in input[10:]]]) or not (crates := [[] for i in range(9)]) or not [crates[j//4].append(line[j]) for line in input[:8] for j in range(1,len(line),4) if line[j].isalpha()] or [crates[move[2]-1].insert(0, crates[move[1]-1].pop(0)) for move in moves for n in range(move[0])] else ''))
print('Day 05 Part 2:', ''.join([c[0] for c in crates] if not (input := open('inputs/day-05.txt').read().split('\n')) or not (moves := [[int(x[1]), int(x[3]), int(x[5])] for x in [y.split(' ') for y in input[10:]]]) or not (crates := [[] for i in range(9)]) or not [crates[j//4].append(line[j]) for line in input[:8] for j in range(1,len(line),4) if line[j].isalpha()] or [crates[move[2]-1].insert(0, item) for move in moves for item in reversed([crates[move[1]-1].pop(0) for n in range(move[0])])] else ''))

# Day 06
print('Day 06 Part 1:', [i+1 for x in [open('inputs/day-06.txt').read()] for i in range(3,len(x)) if len(set(x[i-3:i+1])) == 4][0])
print('Day 06 Part 2:', [i+1 for x in [open('inputs/day-06.txt').read()] for i in range(13,len(x)) if len(set(x[i-13:i+1])) == 14][0])

# Day 07
print('Day 07 Part 1:', sum([x for x in dirs.values() if x <= 100000] if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('inputs/day-07.txt').read().split('\n')]] else ''))
print('Day 07 Part 2:', min([x for x in dirs.values() if x > dirs['//']-40000000]) if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('inputs/day-07.txt').read().split('\n')]] else '')