N, M = [int(x) for x in input().split()]
list_n = [x for x in (input() for _ in range(N))]
dict_n = {y: (int(x) + 1) for x, y in enumerate(list_n)}
list_m = [x for x in (input() for _ in range(M))]

for m in list_m:
    if m.isdigit():
        print(list_n[int(m) - 1])
    else:
        print(dict_n[m])
