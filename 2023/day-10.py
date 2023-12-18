'''
2023 Advent of Code - Day 10 (https://adventofcode.com/2023/day/10)
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

from sys import setrecursionlimit

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-10.txt'

# To match the format of input files for the Basilisk.
q = { 10: open(input_file).read().strip() }


######################### PART 1: MULTI-LINE SOLUTION #########################
grid = [[x for x in row] for row in q[10].strip().split('\n')]
pipe_map = {'|': [(0, -1), (0, 1)], '-': [(1, 0), (-1, 0)], 
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)], 
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)], 
            '.': [], 'S': [(0, -1), (0, 1), (1, 0), (-1, 0)]}

def find_valid_moves(grid, pos, pipe_map, prev_dir=None):
    char = grid[pos[1]][pos[0]]
    valid_directions = pipe_map[char]
    valid_moves = []
    for d in valid_directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        new_char = grid[new_pos[1]][new_pos[0]]
        if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
            if d == (0, -1) and (0, 1) in pipe_map[new_char] and prev_dir != (0, 1):
                valid_moves.append(new_pos)
            if d == (0, 1) and (0, -1) in pipe_map[new_char] and prev_dir != (0, -1):
                valid_moves.append(new_pos)
            if d == (1, 0) and (-1, 0) in pipe_map[new_char] and prev_dir != (-1, 0):
                valid_moves.append(new_pos)
            if d == (-1, 0) and (1, 0) in pipe_map[new_char] and prev_dir != (1, 0):
                valid_moves.append(new_pos)
    return valid_moves

def find_start_char(grid, pos, pipe_map):
    valid_moves = find_valid_moves(grid, pos, pipe_map)
    valid_directions = [(x[0]-pos[0], x[1]-pos[1]) for x in valid_moves]
    for k, v in pipe_map.items():
        if v == valid_directions:
            return k

def solve(grid, pos, pipe_map, visited, prev_dir=None):
    move = find_valid_moves(grid, pos, pipe_map, prev_dir)[0]
    if move == start_pos and len(visited) > 0:
        return visited
    visited.add(move)
    return solve(grid, move, pipe_map, visited, (move[0]-pos[0], move[1]-pos[1]))

start_pos = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]
grid[start_pos[1]][start_pos[0]] = find_start_char(grid, start_pos, pipe_map)

setrecursionlimit(30000)
print('Day 10 Part 1:',len(solve(grid, start_pos, pipe_map, { start_pos }))//2)

########################## PART 1: ONE-LINE SOLUTION ##########################
print('Day 10 Part 1:',(g:=[[x for x in row] for row in q[10].strip().split('\n')],p:={'|':[(0,-1),(0,1)],'-':[(1,0),(-1,0)],'L':[(0,-1),(1,0)],'J':[(0,-1),(-1,0)],'7':[(0,1),(-1,0)],'F':[(0,1),(1,0)],'.':[],'S':[(0,-1),(0,1),(1,0),(-1,0)]},f:=lambda g,c,p,e=None:(r:=g[c[1]][c[0]],s:=p[r],l:=[],[(o:=(c[0]+d[0],c[1]+d[1]),n:=g[o[1]][o[0]],(0<=o[0]<len(g[0]) and 0<=o[1]<len(g)) and ((d==(0,-1) and (0,1) in p[n] and e!=(0,1)) and l.append(o),(d==(0,1) and (0,-1) in p[n] and e!=(0,-1)) and l.append(o),(d==(1,0) and (-1,0) in p[n] and e!=(-1,0)) and l.append(o),(d==(-1,0) and (1,0) in p[n] and e!=(1,0)) and l.append(o))) for d in s]) and l,w:=lambda g,pos,p:[k for k,v in p.items() if v==[(x[0]-pos[0],x[1]-pos[1]) for x in f(g,pos,p)]][0],y:=lambda g,c,p,v,t=None:(v.add(u) or y(g,u,p,v,(u[0]-c[0],u[1]-c[1]))) if (u:=f(g,c,p,t)[0])!=a or not v else v,a:=[(x,y) for y,r in enumerate(g) for x,c in enumerate(r) if c=='S'][0],g[a[1]].__setitem__(a[0],w(g,a,p))) and len(y(g,a,p,{a}))//2)


######################## PART 2: MULTI-LINE SOLUTION ##########################
grid = [[x for x in row] for row in q[10].strip().split('\n')]
pipe_map = {'|': [(0, -1), (0, 1)], '-': [(1, 0), (-1, 0)], 
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)], 
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)], 
            '.': [], 'S': [(0, -1), (0, 1), (1, 0), (-1, 0)]}

def find_valid_moves(grid, pos, pipe_map, prev_dir=None):
    char = grid[pos[1]][pos[0]]
    valid_directions = pipe_map[char]
    valid_moves = []
    for d in valid_directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        new_char = grid[new_pos[1]][new_pos[0]]
        if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
            if d == (0, -1) and (0, 1) in pipe_map[new_char] and prev_dir != (0, 1):
                valid_moves.append(new_pos)
            if d == (0, 1) and (0, -1) in pipe_map[new_char] and prev_dir != (0, -1):
                valid_moves.append(new_pos)
            if d == (1, 0) and (-1, 0) in pipe_map[new_char] and prev_dir != (-1, 0):
                valid_moves.append(new_pos)
            if d == (-1, 0) and (1, 0) in pipe_map[new_char] and prev_dir != (1, 0):
                valid_moves.append(new_pos)
    return valid_moves

def find_start_char(grid, pos, pipe_map):
    valid_moves = find_valid_moves(grid, pos, pipe_map)
    valid_directions = [(x[0]-pos[0], x[1]-pos[1]) for x in valid_moves]
    for k, v in pipe_map.items():
        if v == valid_directions:
            return k

def solve(grid, pos, pipe_map, visited, prev_dir=None):
    move = find_valid_moves(grid, pos, pipe_map, prev_dir)[0]
    if move == start_pos and len(visited) > 0:
        return visited
    visited.add(move)
    return solve(grid, move, pipe_map, visited, (move[0]-pos[0], move[1]-pos[1]))

start_pos = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]
grid[start_pos[1]][start_pos[0]] = find_start_char(grid, start_pos, pipe_map)
visited = solve(grid, start_pos, pipe_map, { start_pos })

contained = set()
for i in range(len(grid)):
    within = 0
    for j in range(len(grid[0])):
        if (j, i) in visited:
            if grid[i][j] in ['|', 'L', 'J']:
                within = not within
        elif within:
            contained.add((j, i))
            
print('Day 10 Part 2:',len(contained))

########################## PART 2: ONE-LINE SOLUTION ##########################
print('Day 10 Part 2:',(g:=[[x for x in row] for row in q[10].strip().split('\n')],p:={'|':[(0,-1),(0,1)],'-':[(1,0),(-1,0)],'L':[(0,-1),(1,0)],'J':[(0,-1),(-1,0)],'7':[(0,1),(-1,0)],'F':[(0,1),(1,0)],'.':[],'S':[(0,-1),(0,1),(1,0),(-1,0)]},f:=lambda g,c,p,e=None:(r:=g[c[1]][c[0]],s:=p[r],l:=[],[(o:=(c[0]+d[0],c[1]+d[1]),n:=g[o[1]][o[0]],(0<=o[0]<len(g[0]) and 0<=o[1]<len(g)) and ((d==(0,-1) and (0,1) in p[n] and e!=(0,1)) and l.append(o),(d==(0,1) and (0,-1) in p[n] and e!=(0,-1)) and l.append(o),(d==(1,0) and (-1,0) in p[n] and e!=(-1,0)) and l.append(o),(d==(-1,0) and (1,0) in p[n] and e!=(1,0)) and l.append(o))) for d in s]) and l,w:=lambda g,c,p:[k for k,v in p.items() if v==[(x[0]-c[0],x[1]-c[1]) for x in f(g,c,p)]][0],y:=lambda g,c,p,v,t=None:(v.add(u) or y(g,u,p,v,(u[0]-c[0],u[1]-c[1]))) if (u:=f(g,c,p,t)[0])!=a or not v else v,a:=[(x,y) for y,r in enumerate(g) for x,c in enumerate(r) if c=='S'][0],g[a[1]].__setitem__(a[0],w(g,a,p)),(v:=y(g,a,p,{ a }),c:=set(),[((w:=0),[((j,i) in v and (g[i][j] in '|LJ' and (w:=not w)),(j,i) not in v and w and c.add((j,i))) for j in range(len(g[0]))]) for i in range(len(g))])) and len(c))