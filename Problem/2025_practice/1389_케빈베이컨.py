from collections import deque

N, M = [int(x) for x in input().split()]
dict_m = {}
list_ans = [0] * (N + 1)

for _ in range(M):
    a, b = [int(x) for x in input().split()]

    if not dict_m.get(a,0):
        dict_m[a] = []
    dict_m[a].append(b)
    if not dict_m.get(b,0):
        dict_m[b] = []
    dict_m[b].append(a)
    

for i in range(1, N + 1):
    dq = deque([(i,0)])
    dict_mini = {}
    s = 0
    while dq:
        pos, dist = dq.popleft()
        nl = dict_m[pos]
        
        for npos in nl:
            if dict_mini.get(npos, 0):
                continue
            dict_mini[npos] = dist + 1
            dq.append((npos, dist + 1))
    for k,v in dict_mini.items():
        s += v
    list_ans[i] = s

ans_idx = 1
for i,an in enumerate(list_ans[1:], 1):
    if an < list_ans[ans_idx]:
        ans_idx = i


print(ans_idx)