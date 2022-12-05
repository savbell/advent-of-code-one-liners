# Day 01
print('Day 01 Part 1:', max([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('./day-01.txt').read().split('\n\n')]]))
print('Day 01 Part 2:', sum(sorted([sum([int(x) for x in g]) for g in [group.split('\n') for group in open('./day-01.txt').read().split('\n\n')]], reverse=True)[0:3]))

# Day 02
print('Day 02 Part 1:', sum([{'A X':3+1,'A Y':6+2,'A Z':0+3,'B X':0+1,'B Y':3+2,'B Z':6+3,'C X':6+1,'C Y':0+2,'C Z':3+3}[x] for x in open('./day-02.txt').read().split('\n')]))
print('Day 02 Part 2:',sum([{'A X':0+3,'A Y':3+1,'A Z':6+2,'B X':0+1,'B Y':3+2,'B Z':6+3,'C X':0+2,'C Y':3+3,'C Z':6+1}[x] for x in open('./day-02.txt').read().split('\n')]))


# Day 03
print('Day 03 Part 1:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(x).intersection(y).pop() for x, y in [[i[:len(i)//2], i[len(i)//2:]] for i in open('./day-03.txt').read().split('\n')]]]))
print('Day 03 Part 2:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(open('./day-03.txt').read().split('\n')[i]).intersection(open('./day-03.txt').read().split('\n')[i+1]).intersection(open('./day-03.txt').read().split('\n')[i+2]).pop() for i in range(0,len(open('./day-03.txt').read().split('\n')),3)]]))

# Day 04
print('Day 04 Part 1:', sum([(x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) for x in [[list(map(int, a.split('-'))), list(map(int, b.split('-')))] for a, b in [x.split(',') for x in open('./day-04.txt').read().split('\n')]]]))
print('Day 04 Part 2:',sum([x[0][0] <= x[1][1] and x[0][1] >= x[1][0] for x in [[list(map(int, a.split('-'))), list(map(int, b.split('-')))] for a, b in [x.split(',') for x in open('./day-04.txt').read().split('\n')]]]))