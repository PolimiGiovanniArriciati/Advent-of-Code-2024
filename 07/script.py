from itertools import product

case = "puzzle.txt", "example.txt"

with open(case[0]) as f:
    puzzle = f.read()

operators = [lambda x, y: x + y, lambda x, y: x * y]


def solve(puzzle, ops):
    answer = 0
    lines = puzzle.split("\n")
    for line in lines:
        result, values = line.split(": ")
        values = list(map(int, values.split(" ")))
        for ops in product(operators, repeat=len(values) - 1):
            left_side = values[0]
            for op, val in zip(ops, values[1:]):
                left_side = op(left_side, val)
            if left_side == int(result):
                answer += int(result)
                break
    return answer


print("partone")  # attempts |12249383342
print(solve(puzzle, operators))


operators += [lambda x, y: int(str(x) + str(y))]
print("parttwo")
print(solve(puzzle, operators))  # attempts |20928985450275
