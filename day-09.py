with open('inputs/day-09.txt') as file:
    moves = file.read().split('\n')

moves = [x.split(' ') for x in moves]

def move(d, h, t):
    if d == 'R':
        if t[0] == h[0]-1:
            if t[1] == h[1]:
                t[0] += 1
            elif t[1] > h[1]:
                t[0] += 1
                t[1] -= 1
            elif t[1] < h[1]:
                t[0] += 1
                t[1] += 1
        h[0] += 1
    elif d == 'L':
        if t[0] == h[0]+1:
            if t[1] == h[1]:
                t[0] -= 1
            elif t[1] > h[1]:
                t[0] -= 1
                t[1] -= 1
            elif t[1] < h[1]:
                t[0] -= 1
                t[1] += 1
        h[0] -= 1
    elif d == 'U':
        if t[1] == h[1]-1:
            if t[0] == h[0]:
                t[1] += 1
            elif t[0] < h[0]:
                t[0] += 1
                t[1] += 1
            elif t[0] > h[0]:
                t[0] -= 1
                t[1] += 1
        h[1] += 1
    elif d == 'D':
        if t[1] == h[1]+1:
            if t[0] == h[0]:
                t[1] -= 1
            elif t[0] < h[0]:
                t[0] += 1
                t[1] -= 1
            elif t[0] > h[0]:
                t[0] -= 1
                t[1] -= 1
        h[1] -= 1

# Part 1
visited = {(0,0)}
h, t = [0,0], [0,0]
for d, n in moves:
    for _ in range(int(n)):
        move(d, t, h)
        visited.add(tuple(t))
print('Day 09 Part 1:', len(visited))

# Part 2 TBD - I'm out today for my birthday :)

# One-line Solutions
print('Day 09 Part 1:', len(visited) if (visited := {(0,0)}) and (h := [0,0]) and (t := [0,0]) and [((d == 'R' and ((t[1] == h[1] and t[0] == h[0]-1 and (t.insert(0, t.pop(0)+1))) or (t[1] > h[1] and t[0] == h[0]-1 and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)-1))) or (t[1] < h[1] and t[0] == h[0]-1 and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)+1))) or 1) and not h.insert(0, h.pop(0)+1)) or (d == 'L' and ((t[1] == h[1] and t[0] == h[0]+1 and (t.insert(0, t.pop(0)-1))) or (t[1] > h[1] and t[0] == h[0]+1 and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)-1))) or (t[1] < h[1] and t[0] == h[0]+1 and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)+1))) or 1) and not h.insert(0, h.pop(0)-1)) or (d == 'U' and ((t[1] == h[1]-1 and t[0] == h[0] and (t.insert(1, t.pop(1)+1))) or (t[1] == h[1]-1 and t[0] < h[0] and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)+1))) or (t[1] == h[1]-1 and t[0] > h[0] and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)+1))) or 1) and h.insert(1, h.pop(1)+1)) or (d == 'D' and ((t[1] == h[1]+1 and t[0] == h[0] and (t.insert(1, t.pop(1)-1))) or (t[1] == h[1]+1 and t[0] < h[0] and not (t.insert(0, t.pop(0)+1) or t.insert(1, t.pop(1)-1))) or (t[1] == h[1]+1 and t[0] > h[0] and not (t.insert(0, t.pop(0)-1) or t.insert(1, t.pop(1)-1))) or 1) and not h.insert(1, h.pop(1)-1)) or 1) and (visited.add(tuple(t))) for d, n in (x.split(' ') for x in open('inputs/day-09.txt').read().split('\n')) for _ in range(int(n))] else '')
