import re

with open("puzzle.txt") as f:
    puzzle = f.read()
corrupted_memory = puzzle

# easy regex
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
ops = re.findall(pattern, corrupted_memory)
mul = lambda x,y : x*y
res = eval('+'.join(ops))
print("pt. 1:")
print(res)

### PART TWO ###

pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
ops = re.findall(pattern, corrupted_memory)
"""
eq_string = (eq_string  .replace("don't()+mul","0*mul") # dont nullifies ALL following operation
                        .replace("do()+mul",   "1*mul") # do confirms the following operation
                        .replace("don't()+",    "")     # dont is ignored otherwise
                        .replace("do()+",       "")     # do is ignored otherwise
                        # .replace("*1*mul",  "+mul")     # if ends with `do` ignore everything else before
)
print("pt. 2:")
print(eval(eq_string))
# 188785850?
"""

eq_string = '+'.join(ops)
# questo é brutto brutto
splitted_eq = eq_string.split("+do")                            # splits both do and donts sengments
splitted_eq = [eq for eq in splitted_eq if "mul" in eq]         # remove the ones that are not followed by a mul
splitted_eq = [eq for eq in splitted_eq if "n't()+" not in eq]  # remove also the ones that are preceded by a dont
splitted_eq = [eq.replace("()+","") for eq in splitted_eq]      # to complete the `do()` that I already started to cut in the `split` 

print("pt. 2:")
print(eval('+'.join(splitted_eq)))