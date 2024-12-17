        #!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from tqdm import tqdm
from itertools import chain
from sys import argv
from collections import defaultdict
from regex import match, findall

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
print(M)

print("\n".join(["".join(row) for row in M]))
print('partone')