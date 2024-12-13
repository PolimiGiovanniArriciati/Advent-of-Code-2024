from tqdm import tqdm
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

def out(x): 
    return regs[x]

detect_loop = False
regs_values = []
program_length = len(operations)
for regs["a"] in tqdm(range(500)):
    sig = ''
    value_a = regs["a"]
    while not detect_loop or len(sig) < 100:
        op = operations[regs['pc']]
        ins = eval(op.split(' ')[0])
        if ins == out:
            sig += str(ins(x))
        elif ins in [inc, dec]:
            x = op.split(' ')[1]
            ins(x)
        else:
            x, y = op.split(' ')[1:]
            ins(x, y)
        regs['pc'] += 1
        if regs['pc'] >= program_length:
            break
        if regs in regs_values:
            detect_loop = True
        regs_values.append(regs.copy())
        
    if sig in "01"*100:
        print(value_a)
        print(sig)
        break
