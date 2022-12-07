with open('inputs/day-06.txt') as file:
    input = file.read()

# Part 1
print('Day 06 Part 1:', [i+1 for i in range(3,len(input)) if len(set(input[i-3:i+1])) == 4][0])

# Part 2
print('Day 06 Part 2:', [i+1 for i in range(13,len(input)) if len(set(input[i-13:i+1])) == 14][0])

# One-line Solutions
print('Day 06 Part 1:', [i+1 for x in [open('inputs/day-06.txt').read()] for i in range(3,len(x)) if len(set(x[i-3:i+1])) == 4][0])
print('Day 06 Part 2:', [i+1 for x in [open('inputs/day-06.txt').read()] for i in range(13,len(x)) if len(set(x[i-13:i+1])) == 14][0])
