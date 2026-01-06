N = int(input())
list_n = [0,0,0]
for _ in range(N):
    a,b,c = [int(x) for x in input().split()]

    na = min(list_n[1], list_n[2]) + a
    nb = min(list_n[0], list_n[2]) + b
    nc = min(list_n[0], list_n[1]) + c

    list_n = [na, nb, nc]

print(min(list_n))
