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

x_max, y_max = (11, 7) if choice == "1" else (101, 103)

robots = []
for line in puzzle.splitlines():
    x,y,dx,dy = tuple(map(int, findall(r"-?\d+", line)))
    robots.append((x,y,dx,dy))

def move(x, y, dx, dy, times):
    x = (x + dx * times)%x_max
    y = (y + dy * times)%y_max
    return x,y

def count_quadrant (positions, quadrant):
    if quadrant == 1:
        return len([_ for x, y in positions if x < x_max//2 and y < y_max//2])
    if quadrant == 2:
        return len([_ for x, y in positions if x > x_max//2 and y < y_max//2])
    if quadrant == 3:
        return len([_ for x, y in positions if x < x_max//2 and y > y_max//2])
    if quadrant == 4:
        return len([_ for x, y in positions if x > x_max//2 and y > y_max//2])

positions = [
    move(x, y, dx, dy, 100)
    for x, y, dx, dy in robots
]

answer = 1
for q in range(1, 5):
    answer *= count_quadrant(positions, q)

# print(positions)
print(answer) # 232_589_280

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
adjacents = lambda x, y: {(x+dx, y+dy) for dx, dy in directions}

def num_adjacents(x, y, positions, visited):
    adj = [num_adjacents(x_, y_, positions-adjacents(x, y)-{(x, y)}, visited|{(x, y)})
                for (x_, y_) in adjacents(x, y)
                if (x_, y_) in positions and
                   (x_, y_) not in visited]
    return 1 if len(adj)==0 else 1+sum(adj)


print(positions)

ok_times = 0
for times in tqdm(range(7543,101*103,1)):
    positions = set()
    [
        positions.add(move(x, y, dx, dy, times))
        for x, y, dx, dy in robots
    ]
    for (x, y) in positions:
        if num_adjacents(x, y, set(positions), set()) > 60:
            ok_times = times
            break
    if ok_times > 0:
        break
    # M = []
    # for _ in range(y_max+1):
    #     M+= [["." for _ in range(x_max+1)]]
    # for x,y in positions:
    #     M[y][x] = "X"
    # print(ok_times)
    # print("\n".join(["".join(row) for row in M]))


M = []
for _ in range(y_max+1):
    M+= [["." for _ in range(x_max+1)]]

for x,y in [move(x, y, dx, dy, ok_times)
            for x, y, dx, dy in robots]:
    M[y][x] = "X"

print(ok_times)
print("\n".join(["".join(row) for row in M]))
input()