with open("puzzle.txt") as f:
    puzzle = f.read()

listone=[[int(elem) for elem in row.split(" ")] for row in puzzle.split("\n")]

l0 = [x[0] for x in listone]
l1 = [x[1] for x in listone]
l0.sort()
l1.sort()

def pos(x):
    return x*-1 if x<0 else x

print("partone")
print(sum([pos(x-y) for x,y in zip(l0, l1)]))

sim_score = 0
for x in l0:
    appereances_x   = len([y for y in l1 if y==x])
    sim_score       += x * appereances_x

print("parttwo")
print(sim_score)