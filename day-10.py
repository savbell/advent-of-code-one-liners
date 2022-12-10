with open('inputs/day-10.txt') as file:
    cmds = file.read().split('\n')

cmds = [y.split(' ') for y in cmds]

# Part 1
def increaseCycle(cycle, n):
    for _ in range(n):
        cycle += 1
        if (cycle+20) % 40 == 0:
            signalStrengths.append(cycle*x)
    return cycle

x, cycle = 1, 0
signalStrengths = []
for c in cmds:
    if c[0] == 'addx':
        cycle = increaseCycle(cycle, 2)
        x += int(c[1])
    elif c[0] == 'noop':
        cycle = increaseCycle(cycle, 1)
print('Day 10 Part 1:', sum(signalStrengths))


# Part 2
def moveSprite(x):
    sprite = ['.'] * 40
    for i in range(x-1,x+2):
        if i < 40 and i >= 0:
            sprite[i] = '#'
    return sprite

def nextCycle():
    if sprite[cycle-((cycle//40)*40)-1] == '#':
        nextPixel = '#'
    else:
        nextPixel = '.'
    crt.append(nextPixel)

x, cycle = 1, 0
sprite = ['#'] * 3 + ['.'] * 37
crt = []
for c in cmds:
    if c[0] == 'addx':
        for _ in range(2):
            cycle += 1
            nextCycle()
        x += int(c[1])
        sprite = moveSprite(x)
    elif c[0] == 'noop':
        cycle += 1
        nextCycle()

print('Day 10 Part 2:')
for i, p in enumerate(crt):
    print(p,end='')
    if (i+1) % 40 == 0:
        print('\n',end='')

# One-line Solutions
print('Day 10 Part 1:', sum(signalStrengths) if not (signalStrengths := []) and (x := 1) and not (cycle := 0) and [[(c[0] == 'addx') and [(cycle := cycle+1) and ((cycle+20) % 40 == 0 and signalStrengths.append(cycle*x)) for _ in range(2)] and (x := x+int(c[1]))] and [(c[0] == 'noop') and [(cycle := cycle+1) and ((cycle+20) % 40 == 0 and signalStrengths.append(cycle*x))]] for c in [y.split(' ') for y in open('inputs/day-10.txt').read().split('\n')]] else '')