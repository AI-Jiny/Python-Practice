from collections import deque
N = int(input())
list_n = [int(x) for x in input().split()]
res = 0
left = 0
dict_n  = {}
for right, n in enumerate(list_n):
    dict_n[list_n[right]] = dict_n.get(list_n[right], 0) + 1
    while len(dict_n) > 2:
        dict_n[list_n[left]] -= 1
        if dict_n[list_n[left]] == 0:
            del dict_n[list_n[left]]
        left += 1

    res = max(res, right - left + 1)

print(res)


