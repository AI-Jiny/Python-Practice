a = [int(input()) for _ in range(9)]
b = sorted(a)
print(b[8])
print(a.index(b[8]) + 1)