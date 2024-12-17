#!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from sys import argv
from functools import lru_cache
from itertools import chain
from time import time

import sys
sys.setrecursionlimit(5000)

if len(argv) == 2:
    _, choice = argv
    in_file = ("puzzle.txt", "example1.txt", "example2.txt",  "example3.txt")[int(choice)]
else:
    raise ValueError(f"Usage: {argv[0]} 0/1 {{0:puzzle, 1:example}}")

with open(in_file) as f:
    puzzle = f.read()

M = [[c for c in line] for line in puzzle.splitlines()]
X, Y = range(len(M)), range(len(M[0]))
initial_position = [(x, y) for x in X for y in Y if M[x][y] == 'S'][0]

adjacent = lambda x, y: [(x + dx, y + dy) for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))]

# @lru_cache(maxsize=None)
# thread pool
from concurrent.futures import ThreadPoolExecutor
threads = ThreadPoolExecutor(20)

def visit(x, y, visited):
    if (x, y) in visited:
        return []
    if M[x][y] == '#':
        return []
    if M[x][y] == 'E':
        return [{(x, y)}]
    visited |= {(x, y)}
    paths = []
    this = {(x, y)}
    while adjacent(x, y).__len__() == 1:
        x, y = adjacent(x, y)[0]
        visited |= {(x, y)}
        this |= {(x, y)}
        
    results = []
    for x1, y1 in adjacent(x, y):
        if (x1, y1) not in visited:
            results += [threads.submit(visit, *(x1, y1, visited.copy() | {(x, y)}))]

    while results != []:
        for r in results:
            if r.done():
                paths += [{(x, y)} | p for p in r.result()]
                results.remove(r)
    return paths
    

x, y = initial_position
start = time()
paths = visit(x, y, set())
print(time()-start, "seconds")

for p in paths:
    pass
    X = [m.copy() for m in M]
    for x_, y_ in p:
        X[x_][y_] = 'X'
    print("\n".join(["".join(row) for row in X]))
    print('-'*10, len(p), '-'*10)

p_score=100_000_000_000
for p in paths:
    p1=p.copy()
    change_of_directions = 0
    xb, yb = initial_position
    p1-={(xb, yb)}
    direction = None
    while len(p1)>0:
        xn, yn = [pos for pos in adjacent(xb, yb) if pos in p1][0]
        if (xn-xb, yn-yb) != direction:
            direction = (xn-xb, yn-yb)
            change_of_directions += 1
        xb, yb = xn, yn
        p1-= {(xb, yb)}
    if p_score>change_of_directions*1000+len(p)+1:
        p_score=change_of_directions*1000+len(p)+1
        best_path = p
        print(p_score)

print(len(paths))
print(len(set(paths)))

print(p_score)
X = [m.copy() for m in M]
for x_, y_ in best_path:
    X[x_][y_] = 'X'

# print("\n".join(["".join(row) for row in X]))
print('-'*10, len(best_path), '-'*10)
print('partone')

"""
X = [m.copy() for m in M]
for x, y in visited:
    X[x][y] = 'X'
print("\n".join(["".join(row) for row in X]))
"""