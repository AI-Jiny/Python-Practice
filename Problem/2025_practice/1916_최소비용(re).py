from collections import deque
from math import inf

N = int(input())
M = int(input())
list_m = [[int(x) for x in input().split()] for _ in range(M)]
start, end = [int(x) for x in input().split()]
dict_m = {}
list_ans = [inf] * (N + 1)
visited =[]

for s, e, c in list_m:
    dict_m.setdefault(s, {})
    dict_m[s][e] = c

def set_node_cost(idx):
    for s,e,c in dict_m[s]:
        if (ne := list_ans[s] + c) < list_ans[e]:
            list_ans[e] = ne
        
    

print(dict_m)


# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5