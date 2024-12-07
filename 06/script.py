case = "puzzle.txt", "example.txt"

with open(case[0]) as f:
    puzzle = f.read()
 
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def rotate(direction, times=1):
    return directions[(directions.index(direction) + times) % 4]


lines = puzzle.split("\n")
lines = [[c for c in line] for line in lines if line]
x_limit, y_limit = len(lines), len(lines[0])

for line in lines:
    assert len(line) == y_limit, f"{len(line)} != {y_limit} for line:\n{line}"

def get_start_direction(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in "^":
                x, y = (i, j)
                return (x, y)

(x,y) = get_start_direction(lines)
start = (x,y)
dx,dy = (-1, 0)

count = 0
while count < 130**2: # puzzle size
    if x+1>=x_limit or y+1>=y_limit or x+dx<0 or y+dy<0:
        lines[x][y] = "X"
        break
    while lines[x+dx][y+dy] == "#":
        dx, dy = rotate((dx, dy))
    else:
        lines[x][y] = "X"
        x += dx
        y += dy
        count += 1

map = '\n'.join([''.join(line) for line in lines])
print("partone") # attempts |5875|5312|5243|5242
print(map.count("X"))

obstacle_positions = set()
possible_obstacle_positions = set()
[[possible_obstacle_positions.add((x,y))
        for y,ch in enumerate(line)
            if ch=='X' and # old path
            (x,y) != start]
        for x,line in enumerate(lines)]

known_obstacle_positions = [(6,3),(7,6),(7,7),(8,1),(8,3),(9,7)]
for pos_obst_pos in possible_obstacle_positions:
    lines = [[c for c in line] for line in puzzle.split("\n") if line]
    lines[pos_obst_pos[0]][pos_obst_pos[1]] = "#"
    x,y = start
    dx,dy = (-1, 0)
    count = 0
    while count < 130**2: # puzzle size
        if x+1>=x_limit or y+1>=y_limit or x+dx<0 or y+dy<0:
            lines[x][y] = "X"
            break
        while lines[x+dx][y+dy] == "#":
            dx, dy = rotate((dx, dy))
        else:
            lines[x][y] = "X"
            x += dx
            y += dy
            count += 1
    
    if count == 130**2:
        obstacle_positions.add(pos_obst_pos)

map = '\n'.join([''.join(line) for line in lines])
print("parttwo")
print(len(obstacle_positions)) # attempts |