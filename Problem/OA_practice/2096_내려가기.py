N = int(input())
list_max = [0, 0, 0]
list_min = [0, 0, 0]

for _ in range(N):
    
    a,b,c = [int(x) for x in input().split()]
    na = max(list_max[0], list_max[1]) + a
    nb = max(list_max) + b
    nc = max(list_max[1], list_max[2]) + c
    list_max = [na, nb, nc]

    na2 = min(list_min[0], list_min[1]) + a
    nb2 = min(list_min) + b
    nc2 = min(list_min[1], list_min[2]) + c

    list_min = [na2, nb2, nc2]

print(max(list_max), min(list_min))
