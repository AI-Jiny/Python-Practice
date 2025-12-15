n = int(input())
list_n = [[int(x), int(y)] for x, y in (input().split() for _ in range(n))]
list_n.sort()
for x, y in list_n:
    print(f"{x} {y}")