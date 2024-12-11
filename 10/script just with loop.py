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

solution = 0
for x,y in starting_points: 
    exploring = {0: [(x,y)]}
    for depth in range(10):
        for (x, y) in exploring[depth]:
            for (x1, y1) in adjacents(x, y):
                if x1 in X and y1 in Y:
                    if value(x1,y1) ==  value(x,y) + 1:
                        if depth+1 not in exploring:
                            exploring[depth+1] = []
                        exploring[depth+1] += [(x1, y1)]
    trailheads = set(exploring[9])
    solution += len(trailheads)

print("partone")  # attempts |778
print(solution)

solution = 0
for x,y in starting_points: 
    exploring = {0: [(x,y)]}
    for depth in range(10):
        for (x, y) in exploring[depth]:
            for (x1, y1) in adjacents(x, y):
                if x1 in X and y1 in Y:
                    if value(x1,y1) ==  value(x,y) + 1:
                        if depth+1 not in exploring:
                            exploring[depth+1] = []
                        exploring[depth+1] += [(x1, y1)]
                        if value(x1,y1) == 9:
                            solution += 1 # count every path to a peak

print("parttwo") # attempts |1925
print(solution)
