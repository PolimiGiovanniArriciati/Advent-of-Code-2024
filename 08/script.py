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
            for x_, y_ in [(x+dx, y+dy), (x-dx, y-dy)]:
                if ((x_ < x_max and y_ < y_max) and
                    (x_ >= 0 and y_ >= 0) and
                    (x_, y_) not in pos):
                    positions.add((x_, y_))
                    if lines[x_][y_] == '.':
                        lines[x_][y_] = '#'

map = '\n'.join([''.join(line) for line in lines])
print("partone")  # attempts |
print(map)
print(len(positions))

positions = set()
count = 0
for c, pos in antennas_pos.items():
    for x, y in pos:
            x_, y_ = x+dx, y+dy
            while (x_ < x_max and y_ < y_max) and (x_ >= 0 and y_ >= 0):
                if (x_, y_) not in pos:
                    positions.add((x_, y_))
                    if lines[x_][y_] == '.':
                        lines[x_][y_] = '#'
                x_, y_ = x_+dx, y_+dy

            x_, y_ = x-dx, y-dy
            while (x_ < x_max and y_ < y_max) and (x_ >= 0 and y_ >= 0):
                if (x_, y_) not in pos:
                    positions.add((x_, y_))
                    count += 1
                    if lines[x_][y_] == '.':
                        lines[x_][y_] = '#' 
                x_, y_ = x_-dx, y_-dy

print("parttwo")
print('\n'.join([''.join(line) for line in lines]))
# i really didn't understand why now the antennas count as antinodes themselves but okay i guess...
print(sum([sum([1 for c in line if c != '.']) for line in lines]))
