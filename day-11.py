def resetMonkeys():
    with open('inputs/day-11.txt') as file:
        monkeys = file.read().split('\n\n')

    monkeys = [[z.split(' ') for z in y[1:]] for y in [x.split('\n') for x in monkeys]]

    for mon in monkeys:
        mon[0] = list(map(int,[a.replace(',','') for a in mon[0][4:]]))
        if mon[1][6] == '*':
            if mon[1][7] == 'old':
                mon[1] = lambda a: a * a
            else:
                mon[1] = lambda a, n=int(mon[1][7]): a * n
        elif mon[1][6] == '+':
            if mon[1][7] == 'old':
                mon[1] = lambda a: a + a
            else:
                mon[1] = lambda a, n=int(mon[1][7]): a + n
        mon[2] = int(mon[2][5])
        mon[3] = int(mon[3][9])
        mon[4] = int(mon[4][9])
        mon.append(0)
    
    return monkeys

# Part 1
monkeys = resetMonkeys()
for _ in range(20):
    for m in monkeys:
        for i in m[0]:
            m[5] += 1
            i = m[1](i) // 3
            if i % m[2] == 0:
                monkeys[m[3]][0].append(i)
            else:
                monkeys[m[4]][0].append(i)
        m[0] = []
inspectionCount = sorted([k[5] for k in monkeys], reverse=True)
print('Day 11 Part 1:', inspectionCount[0] * inspectionCount[1])


# Part 2
monkeys = resetMonkeys()
lcm = 1
for k in monkeys:
    lcm *= k[2]

for _ in range(10000):
    for m in monkeys:
        for i in m[0]:
            m[5] += 1
            i = m[1](i) % lcm
            if i % m[2] == 0:
                monkeys[m[3]][0].append(i)
            else:
                monkeys[m[4]][0].append(i)
        m[0] = []
inspectionCount = sorted([k[5] for k in monkeys], reverse=True)
print('Day 11 Part 2:', inspectionCount[0] * inspectionCount[1])


# One-line Solutions
print('Day 11 Part 1:',inspectionCount[0] * inspectionCount[1] if (monkeys := [[list(map(int,[a.replace(',','') for a in mon[0][4:]])), (mon[1][6] == '*' and ((mon[1][7] == 'old' and (lambda a: a * a)) or (lambda a, n=int(mon[1][7]): a * n))) or ((mon[1][6] == '+' and ((mon[1][7] == 'old' and (lambda a: a + a)) or (lambda a, n=int(mon[1][7]): a + n)))), int(mon[2][5]), int(mon[3][9]), int(mon[4][9]), 0] for mon in [[z.split(' ') for z in y[1:]] for y in [x.split('\n') for x in open('inputs/day-11.txt').read().split('\n\n')]]]) and [[[not (m.insert(5, m.pop(5)+1)) and ((m[1](i) // 3 % m[2] == 0 and not monkeys[m[3]][0].append(m[1](i) // 3)) or not monkeys[m[4]][0].append(m[1](i) // 3)) for i in m[0]] and (not m.insert(1,[]) and m.pop(0)) for m in monkeys] for _ in range(20)] and (inspectionCount := sorted([k[5] for k in monkeys], reverse=True)) else '')
print('Day 11 Part 2:',inspectionCount[0] * inspectionCount[1] if (monkeys := [[list(map(int,[a.replace(',','') for a in mon[0][4:]])), (mon[1][6] == '*' and ((mon[1][7] == 'old' and (lambda a: a * a)) or (lambda a, n=int(mon[1][7]): a * n))) or ((mon[1][6] == '+' and ((mon[1][7] == 'old' and (lambda a: a + a)) or (lambda a, n=int(mon[1][7]): a + n)))), int(mon[2][5]), int(mon[3][9]), int(mon[4][9]), 0] for mon in [[z.split(' ') for z in y[1:]] for y in [x.split('\n') for x in open('inputs/day-11.txt').read().split('\n\n')]]]) and (lcm := 1) and ([lcm := lcm * k[2] for k in monkeys]) and [[[not (m.insert(5, m.pop(5)+1)) and (((m[1](i) % lcm) % m[2] == 0 and not monkeys[m[3]][0].append(m[1](i) % lcm)) or not monkeys[m[4]][0].append(m[1](i) % lcm)) for i in m[0]] and (not m.insert(1,[]) and m.pop(0)) for m in monkeys] for _ in range(10000)] and (inspectionCount := sorted([k[5] for k in monkeys], reverse=True)) else '')