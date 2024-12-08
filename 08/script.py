from string import ascii_letters
from collections import defaultdict

case = "puzzle.txt", "example.txt"

with open(case[0]) as f:
    puzzle = f.read()

lines = [[c for c in line] for line in puzzle.split('\n') if line]
x_max, y_max = len(lines), len(lines[0])
antennas_pos = {c: set() for c in ascii_letters+"0123456789" if puzzle.count(c) > 0}
[[antennas_pos[c].add((x,y)) for y, c in enumerate(line) if c != '.'] for x,line in enumerate(lines)]

differences = defaultdict(set)
positions = set()
for c, pos in antennas_pos.items():
    for x, y in pos:
        for x1, y1 in pos - {(x,y)}:
            differences[(x,y)].add((x1-x, y1-y))
        for dx, dy in differences[(x,y)]:
            for x_, y_ in [(x+dx, y+dy),
                           (x-dx, y-dy)]:
                if (x_ in range(x_max) and
                    y_ in range(y_max) and
                    (x_, y_) not in pos):
                    positions.add((x_, y_))
                    if lines[x_][y_] == '.':
                        lines[x_][y_] = '#'

print("partone")  # attempts |
print('\n'.join([''.join(line) for line in lines]))
print(len(positions))

positions = set()
MAX = max(x_max, y_max)
for c, pos in antennas_pos.items():
    for x, y in pos:
        for dx, dy in differences[(x,y)]:
            for i in range(-MAX, MAX, 1):
                # for i = 0 antinodes are on the antennas
                x_, y_ = x+dx*i, y+dy*i
                if x_ in range(x_max) and y_ in range(y_max):
                    positions.add((x_, y_))
                    if lines[x_][y_] == '.':
                        lines[x_][y_] = '#'

print("parttwo")
print('\n'.join([''.join(line) for line in lines]))
print(len(positions))
