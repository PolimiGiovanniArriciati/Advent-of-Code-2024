with open("puzzle.txt") as f:
    puzzle = f.read()

count = 0
lines = puzzle.split('\n')
len_line = len(lines[0])
for line in lines:
    assert len(line)==len_line, (len_line, len(line), line)

for n, line in enumerate(lines[:-3]):
    for k, letter in enumerate(line[:-3]):
        # horizontal -
        if line[k:k+4] in ("XMAS", "SAMX"):
            count +=1
        
        # diagonal \
        if (lines[n+0][k+0]+
            lines[n+1][k+1]+
            lines[n+2][k+2]+
            lines[n+3][k+3]) in ("XMAS", "SAMX"):
            count+=1
        # diagonal /
        if k >= 3:
            if (lines[n+0][k-0]+
                lines[n+1][k-1]+
                lines[n+2][k-2]+
                lines[n+3][k-3]) in ("XMAS", "SAMX"):
                count+=1
        """
        # This would count the diagonal ones twice...
        if n >= 3 and k >= 3:
            if (lines[n-0][k-0]+
                lines[n-1][k-1]+
                lines[n-2][k-2]+
                lines[n-3][k-3]) in ("XMAS", "SAMX"):
                count+=1
        if n >= 3:
            if (lines[n-0][k+0]+
                lines[n-1][k+1]+
                lines[n-2][k+2]+
                lines[n-3][k+3]) in ("XMAS", "SAMX"):
                count+=1
        """
        # vertical |
        if (lines[n+0][k]+
            lines[n+1][k]+
            lines[n+2][k]+
            lines[n+3][k]) in ("XMAS", "SAMX"):
            count+=1

    for k in range(k+1, k+4):
        # last 3 columns can contain vertical XMASes (excluded by[:-3])
        # note that k is already the last evaluated index
        if (lines[n+0][k]+
            lines[n+1][k]+
            lines[n+2][k]+
            lines[n+3][k]) in ("XMAS", "SAMX"):
            count+=1
        # and diagonal ones (only /)
        if (lines[n+0][k-0]+
            lines[n+1][k-1]+
            lines[n+2][k-2]+
            lines[n+3][k-3]) in ("XMAS", "SAMX"):
                count+=1

# last 3 lines: cannot have the diagonal XMAS...
for n, line in enumerate(lines[-3:]):
    for k, letter in enumerate(line[:-3]):
        if line[k:k+4] in ("XMAS","SAMX"):
            count +=1

print("partone")
print(count)

count = 0
for n, line in enumerate(lines[1:-1]):
    # adjust for offset of the enumerate
    n+=1
    for k, letter in enumerate(line[1:-1]):
        # adjust for offset of the enumerate
        k+=1; 
        if (letter=="A" and
            lines[n-1][k-1]+
            lines[n+1][k-1]+
            lines[n+1][k+1]+
            lines[n-1][k+1]
            in ("MMSS",
                "MSSM", 
                "SSMM", 
                "SMMS")):
                count += 1
print("parttwo")
print(count)