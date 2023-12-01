with open('inputs/day-09.txt') as file:
    moves = file.read().split('\n')

moves = [x.split(' ') for x in moves]

def moveNext(h, t):
    if t[0] < h[0]-1:
        if t[1] == h[1]:
            t[0] += 1
        elif t[1] > h[1]:
            t[0] += 1
            t[1] -= 1
        elif t[1] < h[1]:
            t[0] += 1
            t[1] += 1
    elif t[0] > h[0]+1:
        if t[1] == h[1]:
            t[0] -= 1
        elif t[1] > h[1]:
            t[0] -= 1
            t[1] -= 1
        elif t[1] < h[1]:
            t[0] -= 1
            t[1] += 1
    elif t[1] < h[1]-1:
        if t[0] == h[0]:
            t[1] += 1
        elif t[0] < h[0]:
            t[0] += 1
            t[1] += 1
        elif t[0] > h[0]:
            t[0] -= 1
            t[1] += 1
    elif t[1] > h[1]+1:
        if t[0] == h[0]:
            t[1] -= 1
        elif t[0] < h[0]:
            t[0] += 1
            t[1] -= 1
        elif t[0] > h[0]:
            t[0] -= 1
            t[1] -= 1

def moveHead(d, h):
    if d == 'R':
        h[0] += 1
    if d == 'L':
        h[0] -= 1
    elif d == 'U':
        h[1] += 1
    elif d == 'D':
        h[1] -= 1

# Part 1
visited = set()
h, t = [0,0], [0,0]
for d, n in moves:
    for _ in range(int(n)):
        visited.add(tuple(t))
        moveHead(d, h)
        moveNext(h, t)
print('Day 09 Part 1:', len(visited))

# Part 2
visited = set()
s = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
for d, n in moves:
    for _ in range(int(n)):
        moveHead(d, s[0])
        for i in range(1,10):
            moveNext(s[i-1], s[i])
        visited.add(tuple(s[9]))
print('Day 09 Part 2:', len(visited))

# One-line Solutions
print('Day 09 Part 1:', len(visited) if (visited := {(0,0)}) and (h := [0,0]) and (t := [0,0]) and [((d == 'R' and ((t[1] == h[1] and t[0] == h[0]-1 and (t.insert(0, t.pop(0)+1))) or (t[1] > h[1] and t[0] == h[0]-1 and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)-1))) or (t[1] < h[1] and t[0] == h[0]-1 and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)+1))) or 1) and not h.insert(0, h.pop(0)+1)) or (d == 'L' and ((t[1] == h[1] and t[0] == h[0]+1 and (t.insert(0, t.pop(0)-1))) or (t[1] > h[1] and t[0] == h[0]+1 and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)-1))) or (t[1] < h[1] and t[0] == h[0]+1 and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)+1))) or 1) and not h.insert(0, h.pop(0)-1)) or (d == 'U' and ((t[1] == h[1]-1 and t[0] == h[0] and (t.insert(1, t.pop(1)+1))) or (t[1] == h[1]-1 and t[0] < h[0] and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)+1))) or (t[1] == h[1]-1 and t[0] > h[0] and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)+1))) or 1) and h.insert(1, h.pop(1)+1)) or (d == 'D' and ((t[1] == h[1]+1 and t[0] == h[0] and (t.insert(1, t.pop(1)-1))) or (t[1] == h[1]+1 and t[0] < h[0] and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)-1))) or (t[1] == h[1]+1 and t[0] > h[0] and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)-1))) or 1) and not h.insert(1, h.pop(1)-1)) or 1) and (visited.add(tuple(t))) for d, n in (x.split(' ') for x in open('inputs/day-09.txt').read().split('\n')) for _ in range(int(n))] else '')
print('Day 09 Part 2:', len(visited) if (visited := {(0,0)}) and (s := [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]) and [not ((d == 'R' and s[0].insert(0, s[0].pop(0)+1)) or (d == 'L' and s[0].insert(0, s[0].pop(0)-1)) or (d == 'U' and s[0].insert(1, s[0].pop(1)+1)) or (d == 'D' and s[0].insert(1, s[0].pop(1)-1))) and [(s[i][0] < s[i-1][0]-1 and ((s[i][1] == s[i-1][1] and (s[i].insert(0, s[i].pop(0)+1))) or (s[i][1] > s[i-1][1] and not (s[i].insert(0, s[i].pop(0)+1) or s[i].insert(1, s[i].pop(1)-1))) or (s[i][1] < s[i-1][1] and not (s[i].insert(0, s[i].pop(0)+1) or s[i].insert(1, s[i].pop(1)+1))))) or (s[i][0] > s[i-1][0]+1 and ((s[i][1] == s[i-1][1] and (s[i].insert(0, s[i].pop(0)-1))) or (s[i][1] > s[i-1][1] and not (s[i].insert(0, s[i].pop(0)-1) or s[i].insert(1, s[i].pop(1)-1))) or (s[i][1] < s[i-1][1] and not (s[i].insert(0, s[i].pop(0)-1) or s[i].insert(1, s[i].pop(1)+1))))) or (s[i][1] < s[i-1][1]-1 and ((s[i][0] == s[i-1][0] and (s[i].insert(1, s[i].pop(1)+1))) or (s[i][0] < s[i-1][0] and not (s[i].insert(0, s[i].pop(0)+1) or s[i].insert(1, s[i].pop(1)+1))) or (s[i][0] > s[i-1][0] and not (s[i].insert(0, s[i].pop(0)-1) or s[i].insert(1, s[i].pop(1)+1))))) or (s[i][1] > s[i-1][1]+1 and ((s[i][0] == s[i-1][0] and (s[i].insert(1, s[i].pop(1)-1))) or (s[i][0] < s[i-1][0] and not (s[i].insert(0, s[i].pop(0)+1) or s[i].insert(1, s[i].pop(1)-1))) or (s[i][0] > s[i-1][0] and not (s[i].insert(0, s[i].pop(0)-1) or s[i].insert(1, s[i].pop(1)-1))))) for i in range(1,10)] and (visited.add(tuple(s[9]))) for d, n in (x.split(' ') for x in open('inputs/day-09.txt').read().split('\n')) for _ in range(int(n))] else '')