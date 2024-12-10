#!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from itertools import chain
from sys import argv

if len(argv) == 2:
    _, choice = argv
    input = ("puzzle.txt", "example.txt")[int(choice)]
else:
    raise ValueError(f"Usage: {argv[0]} 0/1 {{0:puzzle, 1:example}}")

with open(input) as f:
    puzzle = f.read()

lines = [[int(i) for i in line] for line in puzzle.split('\n')]
x_max, y_max = len(lines), len(lines[0])

starting_points = set()
[[starting_points.add((x,y)) for y, num in enumerate(line) if num==0] for x, line in enumerate(lines)]
directions = [(0,1), (1,0), (0,-1), (-1,0)]
adjacents = lambda x,y : [(x+dx, y+dy) for (dx, dy) in directions]
X = range(x_max)
Y = range(y_max)
value = lambda x,y : lines[x][y]

def explore(x, y, diff=1):
    if value(x,y) == 9:
        return [[(x, y)]]
    paths = []
    for (x1, y1) in adjacents(x, y):
        if x1 in X and y1 in Y:
            if value(x1,y1) ==  value(x,y) + diff:
                for path in explore(x1, y1, diff):
                    paths += [[(x, y)]+path]
    return paths

solution = 0
for x,y in starting_points: 
    paths = explore(x,y)
    trailheads = set([p[-1] for p in paths])
    solution += len(trailheads)

print("partone")  # attempts |
print(solution)


solution=0
for x,y in starting_points: 
    paths = explore(x,y)
    solution += len(paths)
print("parttwo") # attempts |
print(solution)
