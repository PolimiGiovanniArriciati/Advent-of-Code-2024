#!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from itertools import chain
from sys import argv
from collections import defaultdict

if len(argv) == 2:
    _, choice = argv
    input = ("puzzle.txt", "example1.txt", "example2.txt",  "example3.txt")[int(choice)]
else:
    raise ValueError(f"Usage: {argv[0]} 0/1 {{0:puzzle, 1:example}}")

with open(input) as f:
    puzzle = f.read()

lines = [[c for c in line] for line in puzzle.split("\n")]
y_max, x_max = len(lines), len(lines[0])
Y, X = range(y_max), range(x_max)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
adjacents = lambda x, y: [(x + dx, y + dy)
                          for dx, dy in directions
                            if x+dx in X and y+dy in Y and
                             value(x,y)==value(x+dx,y+dy)]
angulars = lambda x, y: [(x + dx, y + dy)
                         for dx, dy in 
                         [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                         if x+dx in X and y+dy in Y and
                             value(x,y)==value(x+dx,y+dy)]

value = lambda x, y: lines[x][y]

def explore(x, y, visited, depth):
    visited |= {(x,y)}
    for (x1, y1) in adjacents(x, y):
        if (x1, y1) not in visited:
                visited |= explore(x1, y1, visited, depth-1)
    return visited

print("partone")  # attempts |
groups = []
for y in Y:
    for x in X:
        found = False
        for group in groups:
            if (x,y) in group:
                group |= explore(x,y,set(),10)
                found = True
                break
        if not found:
            groups.append(explore(x,y, set(),10))

answer = 0
for group in groups:
    area = len(group)
    perimeter = 0
    for x,y in group:
        perimeter += 4-len([_ for _ in adjacents(x,y)])
    print(value(x,y), area, perimeter)
    answer += area * perimeter
print(answer)

# la cosa migliore da fare e' ridurre un problema complesso in problemi semplici
# come calcolo il numero di lati, con il numero di angoli... come faccio a sapere se ho gia contato un angolo?

adjactents_directions = lambda x, y: {(dx, dy)
                                      for dx, dy in directions
                                        if x+dx in X and y+dy in Y and
                                        value(x+dx, y+dy) == value(x,y)}
def count_corners(x, y, group):
    adj = [(x_,y_) for x_, y_ in adjacents(x, y)]
    if len(adj)==0:
        return 4
    if len(adj)==1:
        return 2
    if len(adj)==2:
        if adjactents_directions(x,y) in [{(1,0), (-1,0)}, {(0, 1), (0,-1)}]:
            return 0
        if len(angulars(x,y)) == 0:
            return 2
        if len(angulars(x,y)) == 4:
            return 1
        for x_a, y_a in angulars(x,y):
            if len([_ for pt in adjacents(x_a, y_a) if pt in adjacents(x,y)])==2: # se l'angolo é di fianco a due adiacenti, allora chiude un angolo?!
                return 1
        return 2
    if len(adj)==3: # T-case
        possible_corners = 2
        for x_a, y_a in angulars(x,y):
            if len([_ for pt in adjacents(x_a, y_a) if pt in adjacents(x,y)])==2: # se l'angolo é di fianco agli adiacenti, allora é 'chiuso'
                possible_corners -= 1
        return possible_corners
    if len(adj)==4:
        possible_corners = 4
        for x_a, y_a in angulars(x,y):
            if len([_ for pt in adjacents(x_a, y_a) if pt in adjacents(x,y)])==2: # se l'angolo é di fianco agli adiacenti, allora é 'chiuso'
                possible_corners -= 1
        return possible_corners
        
    
    
answer = 0
for group in groups:
    area = len(group)
    corners = 0
    for x,y in group:
        corners += count_corners(x,y,group)
    print(value(x,y), area, corners)
    answer += area * (corners)
    
print("parttwo")  # attempts |
print(answer)

""" a mess
        corners += (4 if  == 0 else
                    2 if len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 1 else
                    2 if (len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 1 and
                          len([_ for x,y in angulars(x,y)  if (x,y) in group])) else
                    2 if (len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 1 
                    ) else
                    
                    1 if (len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 3 and
                          len([_ for x,y in angulars(x,y)  if (x,y) in group]) == 1) else
                    2 if (len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 3 and
                          len([_ for x,y in angulars(x,y)  if (x,y) in group]) == 0) else
                    1 if (len([_ for x,y in adjacents(x,y) if (x,y) in group]) == 2 and
                          len([_ for x,y in angulars(x,y)  if (x,y) in group]) == 3) else 
                    0
        )
    """