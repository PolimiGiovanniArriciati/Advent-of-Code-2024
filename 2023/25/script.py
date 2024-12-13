from itertools import chain
file = 'puzzle.txt'
file = 'example.txt'

with open(file) as f:
    puzzle = f.read()

connections = puzzle.split('\n')
connections = [c.split(' ') for c in connections]
connections = [[c[0].strip(':')]+c[1:] for c in connections]


def consolidate(groups):
    groups_consolidated = []
    for group in groups:
        for element in group:
            for group_ in groups:
                if element in group_:
                    groups_consolidated += [group_ | group]
                    break
    return groups_consolidated

groups=[]
for c in connections:
    for element in c:
        found = False
        for g in groups:
            if element in g:
                [g.add(e) for e in c]
                found = True
                break 
        if not found:
            groups += [{element}]
        groups = consolidate(groups)

print(groups)