from collections import defaultdict
import re


with open("puzzle.txt", "r") as f:
    puzzle = f.read()

operations = puzzle.split("\n")

regs = defaultdict(int)

def is_numeric(x):
    return re.fullmatch(r'-?\d+', x)

def cpy(x, y):
    if is_numeric(x):
        regs[y] = int(x)
    else:
        regs[y] = regs[x]

def jnz(x, y):
    y = int(y) if is_numeric(y) else regs[y]
    x = int(x) if is_numeric(x) else regs[x]
    if x != 0:
        regs['pc'] += y - 1

def inc(x): regs[x] += 1
def dec(x): regs[x] -= 1

regs['pc'] = 0
program_length = len(operations)
while True:
    op = operations[regs['pc']]
    ins = op.split(' ')[0]
    if ins in ["inc", "dec"]:
        x = op.split(' ')[1]
        eval(ins)(x)
    else:
        x, y = op.split(' ')[1:]
        eval(ins)(x, y)
    regs['pc'] += 1
    if regs['pc'] >= program_length:
        break

print("partone")
print(regs) # attempts ||318003

regs = defaultdict(int)
regs['c'] = 1
regs['pc'] = 0
program_length = len(operations)
while True:
    op = operations[regs['pc']]
    ins = op.split(' ')[0]
    if ins in ["inc", "dec"]:
        x = op.split(' ')[1]
        eval(ins)(x)
    else:
        x, y = op.split(' ')[1:]
        eval(ins)(x, y)
    regs['pc'] += 1
    if regs['pc'] >= program_length:
        break

print("parttwo")
print(regs) # attempts ||9227657