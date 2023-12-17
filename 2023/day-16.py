'''
2023 Advent of Code - Day 16 (https://adventofcode.com/2023/day/16)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
from sys import setrecursionlimit
import itertools as it


input_file = '2023/day-16.txt'

# To match the format of input files for the Basilisk.
q = { 16: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
grid = [list(x) for x in q[16].strip().split('\n')]

def follow_beam(beam_coord, direction, visited_coords):
    if (beam_coord, direction) not in visited_coords:
        visited_coords.add((beam_coord, direction))
        
    while True:
        if grid[beam_coord[1]][beam_coord[0]] == '.':
            pass
        elif grid[beam_coord[1]][beam_coord[0]] == '/':
            if direction == 'right':
                direction = 'up'
            elif direction == 'left':
                direction = 'down'
            elif direction == 'up':
                direction = 'right'
            elif direction == 'down':
                direction = 'left'
        elif grid[beam_coord[1]][beam_coord[0]] == '\\':
            if direction == 'right':
                direction = 'down'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'up':
                direction = 'left'
            elif direction == 'down':
                direction = 'right'
        elif grid[beam_coord[1]][beam_coord[0]] == '|':
            if direction == 'right':
                visited_coords = follow_beam(beam_coord, 'up', visited_coords)
                direction = 'down'
            elif direction == 'left':
                visited_coords = follow_beam(beam_coord, 'up', visited_coords)
                direction = 'down'
            elif direction == 'up':
                pass
            elif direction == 'down':
                pass
        elif grid[beam_coord[1]][beam_coord[0]] == '-':
            if direction == 'right':
                pass
            elif direction == 'left':
                pass
            elif direction == 'up':
                visited_coords = follow_beam(beam_coord, 'left', visited_coords)
                direction = 'right'
            elif direction == 'down':
                visited_coords = follow_beam(beam_coord, 'left', visited_coords)
                direction = 'right'
        
        if direction == 'right':
            beam_coord = (beam_coord[0]+1, beam_coord[1])
        elif direction == 'left':
            beam_coord = (beam_coord[0]-1, beam_coord[1])
        elif direction == 'up':
            beam_coord = (beam_coord[0], beam_coord[1]-1)
        elif direction == 'down':
            beam_coord = (beam_coord[0], beam_coord[1]+1)

        if (beam_coord, direction) in visited_coords or beam_coord[0] < 0 or beam_coord[0] >= len(grid[0]) or beam_coord[1] < 0 or beam_coord[1] >= len(grid):
            break
        else:
            visited_coords.add((beam_coord, direction))

    return visited_coords

setrecursionlimit(30000)
visited_coords = follow_beam((0,0), 'right', set())
print('Day 16 Part 1:',len(set([x[0] for x in visited_coords])))

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 16 Part 1:',(sys.setrecursionlimit(30000),g:=[list(x) for x in q[16].strip().split('\n')],(f:=lambda c,d,v: ((c,d) not in v and v.add((c,d)),(end:=0)) and [((g[c[1]][c[0]]=='/') and ((d==4) and (d:=1) or (d==3) and (d:=2) or (d==1) and (d:=4) or (d==2) and (d:=3)) or (g[c[1]][c[0]]=='\\') and ((d==4) and (d:=2) or (d==3) and (d:=1) or (d==1) and (d:=3) or (d==2) and (d:=4)) or (g[c[1]][c[0]]=='|') and ((d==4) and (v:=f(c,1,v)) and (d:=2) or (d==3) and (v:=f(c,1,v)) and (d:=2)) or (g[c[1]][c[0]]=='-') and ((d==2) and (d:=4) and (v:=f(c,3,v)) or (d==1) and (d:=4) and (v:=f(c,3,v))),(c:=(c[0]+1,c[1]) if d==4 else (c[0]-1,c[1]) if d==3 else (c[0],c[1]-1) if d==1 else (c[0],c[1]+1)),(((c,d) in v or c[0] < 0 or c[0] >= len(g[0]) or c[1] < 0 or c[1] >= len(g)) and (end:=1)),not (c[0] < 0 or c[0] >= len(g[0]) or c[1] < 0 or c[1] >= len(g)) and v.add((c,d))) for _ in it.takewhile(lambda _: not end,it.count())] and v)) and len(set([x[0] for x in f((0,0),4,set())])))


######################## PART 2: MULTI-LINE SOLUTION ##########################
grid = [list(x) for x in q[16].strip().split('\n')]

def follow_beam(beam_coord, direction, visited_coords):
    if (beam_coord, direction) not in visited_coords:
        visited_coords.add((beam_coord, direction))
        
    while True:
        if grid[beam_coord[1]][beam_coord[0]] == '.':
            pass
        elif grid[beam_coord[1]][beam_coord[0]] == '/':
            if direction == 'right':
                direction = 'up'
            elif direction == 'left':
                direction = 'down'
            elif direction == 'up':
                direction = 'right'
            elif direction == 'down':
                direction = 'left'
        elif grid[beam_coord[1]][beam_coord[0]] == '\\':
            if direction == 'right':
                direction = 'down'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'up':
                direction = 'left'
            elif direction == 'down':
                direction = 'right'
        elif grid[beam_coord[1]][beam_coord[0]] == '|':
            if direction == 'right':
                visited_coords = follow_beam(beam_coord, 'up', visited_coords)
                direction = 'down'
            elif direction == 'left':
                visited_coords = follow_beam(beam_coord, 'up', visited_coords)
                direction = 'down'
            elif direction == 'up':
                pass
            elif direction == 'down':
                pass
        elif grid[beam_coord[1]][beam_coord[0]] == '-':
            if direction == 'right':
                pass
            elif direction == 'left':
                pass
            elif direction == 'up':
                visited_coords = follow_beam(beam_coord, 'left', visited_coords)
                direction = 'right'
            elif direction == 'down':
                visited_coords = follow_beam(beam_coord, 'left', visited_coords)
                direction = 'right'
        
        if direction == 'right':
            beam_coord = (beam_coord[0]+1, beam_coord[1])
        elif direction == 'left':
            beam_coord = (beam_coord[0]-1, beam_coord[1])
        elif direction == 'up':
            beam_coord = (beam_coord[0], beam_coord[1]-1)
        elif direction == 'down':
            beam_coord = (beam_coord[0], beam_coord[1]+1)

        if (beam_coord, direction) in visited_coords or beam_coord[0] < 0 or beam_coord[0] >= len(grid[0]) or beam_coord[1] < 0 or beam_coord[1] >= len(grid):
            break
        else:
            visited_coords.add((beam_coord, direction))

    return visited_coords

max_energized = 0
for x in range(len(grid[0])):
    visited_coords = follow_beam((x,0), 'down', set())
    energized_coords = set([x[0] for x in visited_coords])
    max_energized = len(energized_coords) if len(energized_coords) > max_energized else max_energized
for x in range(len(grid[0])):
    visited_coords = follow_beam((x,len(grid)-1), 'up', set())
    energized_coords = set([x[0] for x in visited_coords])
    max_energized = len(energized_coords) if len(energized_coords) > max_energized else max_energized
for y in range(len(grid)):
    visited_coords = follow_beam((0,y), 'right', set())
    energized_coords = set([x[0] for x in visited_coords])
    max_energized = len(energized_coords) if len(energized_coords) > max_energized else max_energized
for y in range(len(grid)):
    visited_coords = follow_beam((len(grid[0])-1,y), 'left', set())
    energized_coords = set([x[0] for x in visited_coords])
    max_energized = len(energized_coords) if len(energized_coords) > max_energized else max_energized

print('Day 16 Part 2:',max_energized)

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 16 Part 2:',(g:= [list(x) for x in q[16].strip().split('\n')],(f:=lambda c,d,v: ((c,d) not in v and v.add((c,d)),(end:=0)) and [((g[c[1]][c[0]]=='/') and ((d==4) and (d:=1) or (d==3) and (d:=2) or (d==1) and (d:=4) or (d==2) and (d:=3)) or (g[c[1]][c[0]]=='\\') and ((d==4) and (d:=2) or (d==3) and (d:=1) or (d==1) and (d:=3) or (d==2) and (d:=4)) or (g[c[1]][c[0]]=='|') and ((d==4) and (v:=f(c,1,v)) and (d:=2) or (d==3) and (v:=f(c,1,v)) and (d:=2)) or (g[c[1]][c[0]]=='-') and ((d==2) and (d:=4) and (v:=f(c,3,v)) or (d==1) and (d:=4) and (v:=f(c,3,v))),(c:=(c[0]+1,c[1]) if d==4 else (c[0]-1,c[1]) if d==3 else (c[0],c[1]-1) if d==1 else (c[0],c[1]+1)),(((c,d) in v or c[0] < 0 or c[0] >= len(g[0]) or c[1] < 0 or c[1] >= len(g)) and (end:=1)),not (c[0] < 0 or c[0] >= len(g[0]) or c[1] < 0 or c[1] >= len(g)) and v.add((c,d))) for _ in it.takewhile(lambda _: not end,it.count())] and v),(m:=0),[(v:=f((x,0),2,set())) and (m:=len(set([x[0] for x in v])) if len(set([x[0] for x in v])) > m else m) for x in range(len(g[0]))] and [(v:=f((x,len(g)-1),1,set())) and (m:=len(set([x[0] for x in v])) if len(set([x[0] for x in v])) > m else m) for x in range(len(g[0]))] and [(v:=f((0,y),4,set())) and (m:=len(set([x[0] for x in v])) if len(set([x[0] for x in v])) > m else m) for y in range(len(g))] and [(v:=f((len(g[0])-1,y),3,set())) and (m:=len(set([x[0] for x in v])) if len(set([x[0] for x in v])) > m else m) for y in range(len(g))] and m) and m)