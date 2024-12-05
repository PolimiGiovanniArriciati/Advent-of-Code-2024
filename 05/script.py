from tqdm import tqdm 

case = "puzzle.txt", "example.txt"

with open(case[0]) as f:
    puzzle = f.read()

rules, updates = puzzle.split("\n\n")
rules = rules.split("\n")
rules = [list(map(int,rule.split("|"))) for rule in rules] #usavo set non list e mi scombinava l'ordine

updates = updates.split("\n")
updates = [list(map(int, update.split(","))) for update in updates]

"""
# Too complex, i'll evaluate just the rules statically (KISS principle)
class Tree:
    def __init__(self, data, child):
        self.children = [child]
        self.data = data
    def __init__(self, data):
        self.children = []
        self.data = data

pages = []
structured_rules = []

def find_append(tree:Tree, parent:int, child, int):
    # appends the child node after the parent
    # returns False if the parent is not found
    if parent == tree.data:
        parent = Tree(parent, tree.children+[Tree(child)])
        return True, tree
    else:
        founded = False
        trees = []
        for children in tree.children:
            found, tree = find_append(children, parent, child)
            founded += found
            trees += tree

for rule in tqdm(rules):
    first, last = rule
    if last not in pages and first not in pages:
        s_rule = Tree(first, [Tree(last)])
        structured_rules.append(s_rule)
    elif last not in pages and first in pages:
        for i, s_rule in enumerate(structured_rules):
            if first == s_rule.data:
                s_rule = Tree(first, s_rule.children+[Tree(last)])
                structured_rules[i] = s_rule
            else:
                for j, child in enumerate(s_rule.children):
                    if first == child.data:
                        child = Tree(first, child.children+[Tree(last)])
                        
                        
                        

    elif last in pages and first not in pages:
        pass
    elif last in pages and first in pages:
        pass
    pages.add(first)
    pages.add(last)
"""
def mid(list):
    return list[len(list)//2]
        
def pass_rules(rules, update):
    for first, last in rules:
        if first in update and last in update:
            if update.index(first) > update.index(last):
                return False
    return True

answer = 0
tbcorrected = []
for update in updates:
    if pass_rules(rules, update):
        tbcorrected.append(update)
        answer += mid(update)

print("partone") # attempts ||
print(answer)


answer = 0
for update in tbcorrected:
    applied_rules = [(first, last) for (first, last) in rules if ((first in update) and (last in update))]
    while not pass_rules(rules, update):
        for first, last in applied_rules:
            if update.index(first) > update.index(last):
                update[update.index(first)], update[update.index(last)] = last, first
    
    answer += mid(update)

print("parttwo")
print(answer) # attempts ||