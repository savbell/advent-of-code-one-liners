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
