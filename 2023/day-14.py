'''
2023 Advent of Code - Day 14 (https://adventofcode.com/2023/day/14)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

import itertools as it

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-14.txt'

# To match the format of input files for the Basilisk.
q = { 14: open(input_file).read().strip() }

######################### PART 1: MULTI-LINE SOLUTION #########################
# Each platform contains rounded rocks (O) that will roll when the platform is tileted, and cube-shaped rocks (#) which will stay in place. '.' are empty spaces. 
# We are tilting the platform north, so all the rocks (O) will move upwards until they hit a cube (#) or the top of the platform.
platform = [list(x) for x in q[14].strip().split('\n')]
platform.insert(0, ['#']*len(platform[0]))
for i in range(len(platform)):
    for j in range(len(platform[0])):
        if platform[i][j] == 'O':
            for k in range(i-1, -1, -1):
                if platform[k][j] == '#':
                    break
                elif platform[k][j] == '.':
                    platform[k][j] = 'O'
                    platform[k+1][j] = '.'
            else:
                platform[0][j] = '.'
print('Day 14 Part 1:',sum([sum([1 for x in p if x == 'O'])*(i+1) for i,p in enumerate(platform[::-1])]))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 14 Part 1:',sum((platform:=[list(x) for x in q[14].strip().split('\n')]) and not platform.insert(0, ['#']*len(platform[0])) and [[(platform[i][j] == 'O') and [(platform[k][j] == '.') and [(platform[k][j] == '.' and not platform[k].__setitem__(j, 'O') and platform[k+1].__setitem__(j, '.'))] for k in it.takewhile(lambda x: platform[x][j] != '#',range(i-1, -1, -1))] for j in range(len(platform[0]))] for i in range(len(platform))] and [sum([1 for x in p if x == 'O'])*(i+1) for i,p in enumerate(platform[::-1])]))


######################## PART 2: MULTI-LINE SOLUTION ##########################
def tilt_platform(platform, direction):
    if direction == 'north':
        for i in range(len(platform)):
            for j in range(len(platform[0])):
                if platform[i][j] == 'O':
                    for k in range(i-1, -1, -1):
                        if platform[k][j] == '#':
                            break
                        elif platform[k][j] == '.':
                            platform[k][j] = 'O'
                            platform[k+1][j] = '.'
                    else:
                        platform[0][j] = '.'
    elif direction == 'west':
        for i in range(len(platform)):
            for j in range(len(platform[0])):
                if platform[i][j] == 'O':
                    for k in range(j-1, -1, -1):
                        if platform[i][k] == '#':
                            break
                        elif platform[i][k] == '.':
                            platform[i][k] = 'O'
                            platform[i][k+1] = '.'
                    else:
                        platform[i][0] = '.'
    elif direction == 'south':
        for i in range(len(platform)-1, -1, -1):
            for j in range(len(platform[0])):
                if platform[i][j] == 'O':
                    for k in range(i+1, len(platform)):
                        if platform[k][j] == '#':
                            break
                        elif platform[k][j] == '.':
                            platform[k][j] = 'O'
                            platform[k-1][j] = '.'
                    else:
                        platform[-1][j] = '.'
    elif direction == 'east':
        for i in range(len(platform)):
            for j in range(len(platform[0])-1, -1, -1):
                if platform[i][j] == 'O':
                    for k in range(j+1, len(platform[0])):
                        if platform[i][k] == '#':
                            break
                        elif platform[i][k] == '.':
                            platform[i][k] = 'O'
                            platform[i][k-1] = '.'
                    else:
                        platform[i][-1] = '.'
    return platform

def plat_to_string(platform):
    return 'y'.join(['x'.join(x) for x in platform])

def string_to_plat(string):
    return [x.split('x') for x in string.split('y')]

platform = [['#'] + list(x) + ['#'] for x in q[14].strip().split('\n')]
platform.insert(0, ['#']*len(platform[0]))
platform.append(['#']*len(platform[0]))
size = len(platform)

stored_states = [plat_to_string(platform)]
while True:
    platform = tilt_platform(platform, 'north')
    platform = tilt_platform(platform, 'west')
    platform = tilt_platform(platform, 'south')
    platform = tilt_platform(platform, 'east')
    if plat_to_string(platform) in stored_states:
        break
    stored_states.append(plat_to_string(platform))

first_occurence = stored_states.index(plat_to_string(platform))
cycles = len(stored_states) - first_occurence
platform = string_to_plat(stored_states[(1000000000 - first_occurence) % cycles + first_occurence])

print('Day 14 Part 2:',sum([sum([1 for x in p if x == 'O'])*(i) for i,p in enumerate(platform[::-1])]))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 14 Part 2:',sum((tilt_platform:=lambda platform,direction: (((direction == 'north') and [[(platform[i][j] == 'O') and [(platform[k][j] == '.') and [(platform[k][j] == '.' and not platform[k].__setitem__(j, 'O') and platform[k+1].__setitem__(j, '.'))] for k in it.takewhile(lambda x: platform[x][j] != '#',range(i-1, -1, -1))] for j in range(len(platform[0]))] for i in range(len(platform))]) or ((direction == 'west') and [[(platform[i][j] == 'O') and [(platform[i][k] == '.') and [(platform[i][k] == '.' and not platform[i].__setitem__(k, 'O') and platform[i].__setitem__(k+1, '.'))] for k in it.takewhile(lambda x: platform[i][x] != '#',range(j-1, -1, -1))]] for i in range(len(platform)) for j in range(len(platform[0]))]) or (direction == 'south') and [(platform[i][j] == 'O') and [(platform[k][j] == '.') and [(platform[k][j] == '.' and not platform[k].__setitem__(j, 'O') and platform[k-1].__setitem__(j, '.'))] for k in it.takewhile(lambda x: platform[x][j] != '#',range(i+1, len(platform)))] for j in range(len(platform[0])) for i in range(len(platform)-1, -1, -1)] or (direction == 'east') and [(platform[i][j] == 'O') and [(platform[i][k] == '.') and [(platform[i][k] == '.' and not platform[i].__setitem__(k, 'O') and platform[i].__setitem__(k-1, '.'))] for k in it.takewhile(lambda x: platform[i][x] != '#',range(j+1, len(platform[0])))] for i in range(len(platform)) for j in range(len(platform[0])-1, -1, -1)]) and platform) and (plat_to_string:=lambda platform: 'y'.join(['x'.join(x) for x in platform])) and (string_to_plat:=lambda string: [x.split('x') for x in string.split('y')]) and (platform:=[['#'] + list(x) + ['#'] for x in q[14].strip().split('\n')]) and not platform.insert(0, ['#']*len(platform[0])) and not platform.append(['#']*len(platform[0])) and (stored_states:=[plat_to_string(platform)]) and [(platform:=tilt_platform(tilt_platform(tilt_platform(tilt_platform(platform, 'north'), 'west'), 'south'), 'east')) and (plat_to_string(platform) not in stored_states) and stored_states.append(plat_to_string(platform)) for _ in it.takewhile(lambda x: plat_to_string(platform) not in stored_states[:-1], it.repeat(None))] and (platform:=string_to_plat(stored_states[(1000000000 - (first_occurence:=stored_states.index(plat_to_string(platform)))) % (len(stored_states) - first_occurence) + first_occurence])) and [sum([1 for x in p if x == 'O'])*(i) for i,p in enumerate(platform[::-1])]))
