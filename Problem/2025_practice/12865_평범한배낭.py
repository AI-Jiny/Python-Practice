N, k = [int(x) for x in input().split()]
list_n = [[int(w), int(v)] for w, v in (input().split() for _ in range(N))]
list_n.sort(key=lambda x: (x[1] / x[0], x[0]))
answer = 0
dict_v = {}

print(list_n)
