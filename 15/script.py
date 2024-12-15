#!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from sys import argv

if len(argv) == 2:
    _, choice = argv
    in_file = ("puzzle.txt", "example1.txt", "example2.txt",  "example3.txt")[1]#[int(choice)]
else:
    raise ValueError(f"Usage: {argv[0]} 0/1 {{0:puzzle, 1:example}}")

with open(in_file) as f:
    puzzle = f.read()

puzzle = puzzle.split("\n\n")
map = [[c for c in line] for line in puzzle[0].split("\n")]
moves = ''.join(puzzle[1].split("\n"))
y_max, x_max = len(map), len(map[0])
wall, box, empty, robot = "#", "O", ".", "@"
initial_position = [(x, y) for x in range(x_max)  for y in range(y_max) if map[y][x] == robot][0]

directions = { '>': (0, 1),
               'v': (1, 0),
               '<': (0, -1),
               '^': (-1, 0)
               }

def move(x, y, direction):
    dx, dy = directions[direction]
    x1, y1 = x + dx, y + dy
    if map[x1][y1] == empty:
        map[x][y] = empty
        map[x1][y1] = robot
        return x1, y1
    if map[x1][y1] == wall:
        return x, y
    while map[x1][y1] == box:
        x1, y1 = x1 + dx, y1 + dy
        if map[x1][y1] == empty:
            map[x1][y1] = box
            map[x][y] = empty
            map[x+dx][y+dy] = robot
            return x+dx, y+dy
        if map[x1][y1] == wall:
            return x, y

x, y = initial_position
for dir in moves:
    x, y = move(x, y, dir)

# compute checksum for sumbission
answer = sum([y*100+x for x in range(x_max) for y in range(y_max) if map[y][x] == box])
# print('\n'.join(''.join(row) for row in map))

##########################################################################################

if len(argv) == 2:
    _, choice = argv
    in_file = ("puzzle large.txt", "example large Jaiz0.txt", "example large.txt", "example large 2.txt")[int(choice)]
else:
    raise ValueError(f"Usage: {argv[0]} 0/1 {{0:puzzle, 1:example}}")
with open(in_file) as f:
    puzzle = f.read()

puzzle = puzzle.split("\n\n")
map = [[c for c in line] for line in puzzle[0].split("\n")]
moves = ''.join(puzzle[1].split("\n"))
y_max, x_max = len(map), len(map[0])
wall, box, empty, robot = "#", "[]", ".", "@"
initial_position = [(y, x) for x in range(x_max)  for y in range(y_max) if map[y][x] == robot][0]

def move(x, y, dir):
    # assert map[x][y] == robot
    dx, dy = directions[dir]
    x1, y1 = x + dx, y + dy
    if map[x1][y1] == empty:
        map[x][y] = empty
        map[x1][y1] = robot
        return x1, y1
    if map[x1][y1] == wall:
        return x, y
    if map[x1][y1] in box:
        if can_move_box(x1, y1, dir):
            left_side = expand(x1, y1, dir)
            moved_left_side = [(x1+dx, y1+dy) for x1, y1 in left_side]
            right_side = [(x1, y1+1) for x1, y1 in left_side]
            moved_right_side = [(x1+dx, y1+dy) for x1, y1 in right_side]
            for (x1, y1), (x2, y2) in zip(left_side, right_side):
                map[x1][y1] = empty
                map[x2][y2] = empty
            for (x1, y1), (x2, y2) in zip(moved_left_side, moved_right_side):
                map[x1][y1] = '['
                map[x2][y2] = ']'
            map[x][y] = empty
            map[x+dx][y+dy] = robot  
            return x+dx, y+dy
        return x, y

def can_move_box(x, y, dir):
    # break at (x,y,dir)==(7,10,'^')
    dx, dy = directions[dir]
    x1, y1 = x + dx, y + dy
    if map[x][y] == ".":
        return True
    if map[x][y] == "]":
        return can_move_box(x, y-1, dir)
    if dir in "<":
        if map[x1][y1] == wall:
            return False
        if map[x1][y1] == empty:
            return True
        return can_move_box(x1, y1-1, dir) # check for '[' side
    x2, y2 = x + dx, y + 1 + dy # other ']' side of the box
    if dir in ">":
        if map[x2][y2] == wall:
            return False
        if map[x2][y2] == empty:
            return True
        return can_move_box(x2, y2, dir)
    if map[x1][y1] == wall or map[x2][y2] == wall:
        return False
    if map[x1][y1] == empty and map[x2][y2] == empty:
        return True
    return can_move_box(x1, y1, dir) and can_move_box(x2, y2, dir)
    
def expand(x, y, dir):
    dx, dy = directions[dir]
    x1, y1 = x + dx, y + dy
    if map[x][y] == ".":
        return []
    if map[x][y] == "]":
        return expand(x, y-1, dir)
    if dir in "<":
        if map[x1][y1] == empty:
            return [(x,y)]
        return [(x,y)] + expand(x1, y1-1, dir) # check for '[' side
    x2, y2 = x + dx, y + 1 + dy # other ']' side of the box
    if dir in ">":
        if map[x2][y2] == empty:
            return [(x,y)]
        return [(x,y)]+expand(x2, y2, dir)
    if map[x1][y1] == empty and map[x2][y2] == empty:
        return [(x,y)]
    return [(x,y)] + expand(x1, y1, dir) + expand(x2, y2, dir)

x, y = initial_position
for k, dir in enumerate(moves):
    # print(dir, k)
    x, y = move(x, y, dir)
    # map[x][y] = dir
    # print('\n'.join(''.join(row) for row in map))
    if '[[' in '\n'.join(''.join(row) for row in map):
        raise ValueError("oops")

# `example large` solution
answer = sum([y*100+x for x in range(x_max) for y in range(y_max) if map[y][x] == '['])
print('\n'.join(''.join(row) for row in map))
print("parttwo")
print(answer)