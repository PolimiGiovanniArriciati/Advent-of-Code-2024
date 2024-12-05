with open("puzzle.txt") as f:
    puzzle = f.read()

reports=[[int(elem) for elem in row.split(" ")] for row in puzzle.split("\n")]

def is_report_ok(report):
    if report[0] < report[1]:
        # increasing
        for i, r in enumerate(report[:-1]):
            if r not in range(report[i+1]-3, report[i+1]) or r == report[i+1]:
                return False
    elif report[0] > report[1]:
        # decreasing
        for i, r in enumerate(report[:-1]):
            if report[i+1] not in range(r-3, r) or r == report[i+1]:
                return False
    else:
        return False
    return True

good_reports = 0
for report in reports:
        good_reports += 1 if is_report_ok(report) else 0
    
print("partone")
print(good_reports)

good_reports = 0
for report in reports:
    if is_report_ok(report):
        good_reports += 1
    else:
        for i, r in enumerate(report):
            if is_report_ok(report[:i]+report[i+1:]):
                good_reports+=1
                break

print("parttwo")
print(good_reports)