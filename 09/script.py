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

out=[]
for i, ch in zip(puzzle, range(0, len(puzzle)*2)):
        if ch % 2 == 0:
            out += [ch//2]*int(i)
        else:
            out += ["."]*int(i)


last_full = len(out) - 1
for i in range(0, len(out)):
    if out[i] == '.':
        for j in range(last_full, i-1, -1):
            if out[j] != '.':
                out[i], out[j] = out[j], out[i]
                last_full = j
                break
            elif j == i:
                break
    if last_full == i:
            break

chksum = 0 

print(out)
for k, v in enumerate(out):
    chksum += (k * v) if v != '.' else 0

print("partone")  # attempts |5638933623|5037014738 wo0|5501086049 wol.|6360094256423
print(chksum)


out = []
for i, ch in zip(puzzle, range(0, len(puzzle)*2)):
        if ch % 2 == 0:
            out += [[ch//2]*int(i)]
        elif i != '0':
            out += [["."]*int(i)]

i = 0
for i in range(0, len(out)):
    if '.' in out[i]:
        empty = out[i]
        for j in range(len(out) - 1, i, -1):
            file = out[j]
            if '.' not in file and len(file) == len(empty):
                out[i], out[j] = file, empty
                break
            elif '.' not in file and len(file) < len(empty):
                out[i+2:] = out[i+1:]
                out[i+1] = empty[len(file):]
                out[i], out[j+1] = file, empty[:len(file)]
                break

out = [v for v in chain(*out)]
print(out)

chksum = 0 
for k, v in enumerate(out):
    chksum += (k * v) if v != '.' else 0
    
print("parttwo") # attempts |
print(chksum)
