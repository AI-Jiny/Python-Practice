from collections import deque

N, M, V = [int(x) for x in input().split()]

list_m = [[int(x),int(y)] for x, y in (input().split() for _ in range(M))]
dict_n = {}

for x, y in list_m:
    dict_n.setdefault(x, []).append(y)
    dict_n.setdefault(y, []).append(x)

for v in dict_n.values():
    v.sort()

visited_bfs = [V]
visited_dfs = []
def bfs(start):
    dq = deque([])
    dq.append(start)
    while dq:
        nq = dq.popleft()
        for n in dict_n.get(nq, []):
            if n not in visited_bfs:
                visited_bfs.append(n)
                dq.append(n)


def dfs(start):
    visited_dfs.append(start)
    for nxt in dict_n.get(start, []):
        if nxt not in visited_dfs:
            dfs(nxt)

bfs(V)
dfs(V)

print(" ".join([str(x) for x in visited_dfs]))
print(" ".join([str(x) for x in visited_bfs]))