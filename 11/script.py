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

def apply_rules(stones, times):
    if times == 0:
        return input
    new_stones = []
    for stone in stones:
        stone_digits = len(str(stone))
        if stone == 0:
            new_stones += [1]
        elif stone_digits % 2 == 0:
            new_stones += [stone//(10**(stone_digits//2)), stone%(10**(stone_digits//2))]
        else:
            ns = stone*2024
            new_stones += [ns] 
    return apply_rules(new_stones, times-1)

from functools import lru_cache

@lru_cache(maxsize=None)
def sum_len_apply_rules(stone, times):
    if times == 0:
        return 1
    stone_digits = len(str(stone))
    if stone == 0:
        return sum_len_apply_rules(1, times-1) 
    elif stone_digits % 2 == 0:
        return (sum_len_apply_rules(stone//(10**(stone_digits//2)), times-1) + 
                sum_len_apply_rules(stone %(10**(stone_digits//2)), times-1))
    else:
        return sum_len_apply_rules(stone*2024, times-1)
    

stones = [int(i) for i in puzzle.split(' ')]
print("partone")  # attempts |
print(sum([sum_len_apply_rules(stone, 25) for stone in stones]))


print("parttwo")  # attempts |
print(sum([sum_len_apply_rules(stone, 75) for stone in stones]))