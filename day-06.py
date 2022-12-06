with open('inputs/day-06.txt') as file:
    input = file.read()

# Part 1
print([i+1 for i in range(3,len(input)) if len(set(input[i-3:i+1])) == 4][0])

# Part 2
print([i+1 for i in range(13,len(input)) if len(set(input[i-13:i+1])) == 14][0])