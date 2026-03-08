ans = []
while True:
    lines = input()
    if lines == "0 0 0":
        break

    lines = [int(x) for x in lines.split()]
    line_set = set(lines)
    max_line = 0
    total = 0
    
    for line in lines:
        if max_line < line:
            max_line = line
        total += line

    if total  <= max_line * 2:
        ans.append("invalid")
    elif len(line_set) == 1:
        ans.append("Equilateral")
    elif len(line_set) == 2:
        ans.append("Isosceles")
    else:
        ans.append("Scalene")

for an in ans:
    print(an)
# 7 7 7
# 6 5 4
# 3 2 5
# 6 2 6
# 0 0 0
