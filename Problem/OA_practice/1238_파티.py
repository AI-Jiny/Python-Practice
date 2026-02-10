import sys
import heapq
from math import inf

input = sys.stdin.readline

n, m, x = [int(x) for x in input().split()]
graph_go = [[] for _ in range(n + 1)]
graph_back = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = [int(x) for x in input().split()]
    graph_go[s].append((c, e))
    graph_back[e].append((c, s))


def exec_dij(graph):
    heap = []
    heapq.heappush(heap, (0, x))
    res = [inf] * (n + 1)
    res[x] = 0
    while heap:
        c, e = heapq.heappop(heap)
        if res[e] < c:
            continue

        for cc, ne in graph[e]:
            nc = c + cc
            if nc < res[ne]:
                res[ne] = nc
                heapq.heappush(heap, (nc, ne))
    return res[1:]

go = exec_dij(graph_go)
back = exec_dij(graph_back)
ans = 0
for a,b in zip(go, back):
    if a + b > ans:
        ans = a + b

print(ans)    
