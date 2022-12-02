with open('./day-02.txt') as file:
    rounds = file.read().split('\n')

# Part 1
outcomeP1 = {
    'A X': 3+1,
    'A Y': 6+2,
    'A Z': 0+3,
    'B X': 0+1,
    'B Y': 3+2,
    'B Z': 6+3,
    'C X': 6+1,
    'C Y': 0+2,
    'C Z': 3+3,
}

# Part 2
outcomeP2 = {
    'A X': 0+3,
    'A Y': 3+1,
    'A Z': 6+2,
    'B X': 0+1,
    'B Y': 3+2,
    'B Z': 6+3,
    'C X': 0+2,
    'C Y': 3+3,
    'C Z': 6+1,
}

resultP1 = sum(map(lambda x: outcomeP1[x], rounds))
print(resultP1)

resultP2 = sum(map(lambda x: outcomeP2[x], rounds))
print(resultP2)