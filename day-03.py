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
print(priorityTotal)

# Part 2
priorityTotal = 0
for i in range(0,len(rucksacks),3):
    priorityTotal += findPriority(set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2]).pop())
print(priorityTotal)