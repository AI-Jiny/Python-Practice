def sum_gen(N):
    return sum(n for n in range(1, N + 1))
import math
a = int(input())
for i in range(a):
    b = input()
    b = [v for v in b.replace("O", "1").split("X") if v]
    c = list(map(int, b))
    for i in range(len(c)):
        c[i] = sum_gen(int(math.log10(c[i])) + 1)
    print(sum(c))