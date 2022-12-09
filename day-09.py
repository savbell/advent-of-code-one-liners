with open('inputs/day-09.txt') as file:
    moves = file.read().split('\n')

moves = [x.split(' ') for x in moves]

def move(d, t, h):
    if d == 'R':
        if t[1] == h[1] and t[0] == h[0]-1:
            t[0] += 1
        elif t[1] > h[1] and t[0] == h[0]-1:
            t[0] += 1
            t[1] -= 1
        elif t[1] < h[1] and t[0] == h[0]-1:
            t[0] += 1
            t[1] += 1
        h[0] += 1
    elif d == 'L':
        if t[1] == h[1] and t[0] == h[0]+1:
            t[0] -= 1
        elif t[1] > h[1] and t[0] == h[0]+1:
            t[0] -= 1
            t[1] -= 1
        elif t[1] < h[1] and t[0] == h[0]+1:
            t[0] -= 1
            t[1] += 1
        h[0] -= 1
    elif d == 'U':
        if t[1] == h[1]-1 and t[0] == h[0]:
            t[1] += 1
        elif t[1] == h[1]-1 and t[0] < h[0]:
            t[0] += 1
            t[1] += 1
        elif t[1] == h[1]-1 and t[0] > h[0]:
            t[0] -= 1
            t[1] += 1
        h[1] += 1
    elif d == 'D':
        if t[1] == h[1]+1 and t[0] == h[0]:
            t[1] -= 1
        elif t[1] == h[1]+1 and t[0] < h[0]:
            t[0] += 1
            t[1] -= 1
        elif t[1] == h[1]+1 and t[0] > h[0]:
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
