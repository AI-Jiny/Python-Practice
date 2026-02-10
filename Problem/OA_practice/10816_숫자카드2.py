N = int(input())
list_n = [int(n) for n in input().split()]
M = int(input())
list_m = [int(m) for m in input().split()]

dict_n = {}
for n in list_n:
    dict_n[n] = dict_n.get(n, 0) + 1

answer = " ".join(str(dict_n.get(m, 0)) for m in list_m)

print(answer)


