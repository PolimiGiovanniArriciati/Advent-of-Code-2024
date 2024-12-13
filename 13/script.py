#!/Users/gio/hacking/aoc/.venv/bin/python3 script.py 1
from tqdm import tqdm
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

button_a = lambda machine: [int(x.split('+')[1])
                            for x in machine.split('\n')[0]
                                            .strip("Button A: ")
                                            .split(', ')]
button_b = lambda machine: [int(x.split('+')[1])
                            for x in machine.split('\n')[1]
                                            .strip("Button B: ")
                                            .split(', ')]
prize = lambda machine: [int(x.split('=')[1])
                            for x in machine.split('\n')[2]
                                            .strip("Prize: ")
                                            .split(', ')]
                            
machines = [(button_a(m), 
             button_b(m),
             prize(m)) for m in puzzle.split("\n\n")]

cost = 0
for m in machines:
    possible_values = []
    possible_values_ = []
    x,y = 0,1
    expensv = m[0] # A button costs 3 token
    cheap = m[1] # B button costs 1 token
    min_cost = 0
    for k in range(0, m[2][x]+1, cheap[x]):
        if (m[2][x] - k) % expensv[x] == 0:
            j = (m[2][x] - k) // expensv[x]
            k = k // cheap[x]
            possible_values += [(k, j)]
    for k,j in possible_values:
        if m[1][y]*k + m[0][y]*j == m[2][y]:
            possible_values_ += [(k, j)]
            min_cost = possible_values_[0][1]*3 + possible_values_[0][0]*1
    for k,j in possible_values_:
        if j*3 + k*1 < min_cost:
            min_cost = j*3 + k*1
    cost += min_cost

print("partone")  # attempts |
print(cost)

prize_pt_2 = lambda machine: [int(x.split('=')[1])+10000000000000
                            for x in machine.split('\n')[2]
                                            .strip("Prize: ")
                                            .split(', ')]
                            
machines = [(button_a(m), 
             button_b(m),
             prize_pt_2(m)) for m in puzzle.split("\n\n")]

cost = 0
for expensv, cheap, total  in tqdm(machines):
    x,y = 0,1
    min_cost = 0
    reminder = total[x] % cheap[x]
    for i in range(cheap[x]):
        if (reminder + cheap[x]*i) % expensv[x] == 0:
            cnt_cheap = (total[x]//cheap[x]) - i
            cnt_expen = (total[x]-cnt_cheap*cheap[x])//expensv[x]
            if (expensv[y]*cnt_expen + cheap[y]*cnt_cheap) == total[y]:
                cost += cnt_cheap*1 + cnt_expen*3
                break
    for i in range(cheap[x]):
        if (reminder + cheap[x]*i) % expensv[x] == 0:
            cnt_cheap = (total[x]//cheap[x]) - i
            cnt_expen = (total[x]-cnt_cheap*cheap[x])//expensv[x]
            if (expensv[y]*cnt_expen + cheap[y]*cnt_cheap) == total[y]:
                cost += cnt_cheap*1 + cnt_expen*3
                break
    
print("parttwo")  # attempts |
print(cost)