N = int(input())
balls = input()
red = balls.count("R")
blue = N - red

a = blue - balls.index("R")
b = red - balls.index("B")
c = blue - balls[::-1].index("R")
d = red - balls[::-1].index("B")
ans = min(a, b, c, d)

print(ans)
# 8
# BBRBBBBR
