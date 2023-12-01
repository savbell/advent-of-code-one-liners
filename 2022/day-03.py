def findPriority(item):
    if item.islower():
        return ord(item)-96
    else:
        return ord(item)-38

with open('inputs/day-03.txt') as file:
    rucksacks = file.read().split('\n')

# Part 1
splitRucksacks = [[i[:len(i)//2], i[len(i)//2:]] for i in rucksacks]
sharedItems = [set(x).intersection(y).pop() for x, y in splitRucksacks]
priorityTotal = sum([findPriority(x) for x in sharedItems])
print('Day 03 Part 1:', priorityTotal)

# Part 2
priorityTotal = 0
for i in range(0,len(rucksacks),3):
    priorityTotal += findPriority(set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2]).pop())
print('Day 03 Part 2:', priorityTotal)

# One-line Solutions
print('Day 03 Part 1:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(x).intersection(y).pop() for x, y in [[i[:len(i)//2], i[len(i)//2:]] for i in open('inputs/day-03.txt').read().split('\n')]]]))
print('Day 03 Part 2:', sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(open('inputs/day-03.txt').read().split('\n')[i]).intersection(open('inputs/day-03.txt').read().split('\n')[i+1]).intersection(open('inputs/day-03.txt').read().split('\n')[i+2]).pop() for i in range(0,len(open('inputs/day-03.txt').read().split('\n')),3)]]))
