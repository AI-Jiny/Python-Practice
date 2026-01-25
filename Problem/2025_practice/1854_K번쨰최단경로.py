import sys
import heapq
from math import inf
input = sys.stdin.readline

n, m, k = [int(x) for x in input().split()]
graph = [[] for _ in range(n + 1)]
res = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = [int(x) for x in input().split()]
    graph[s].append((c, e))

heap = []
heapq.heappush(res[1], 0)
heapq.heappush(heap, (0, 1))

while heap:
    c, e = heapq.heappop(heap)
    for cc, ne in graph[e]:
        nc = c + cc
        
        if len(res[ne]) >= k:
            if -(res[ne][0]) <= nc:
                continue
            else:
                heapq.heappop(res[ne])
        heapq.heappush(res[ne], -nc)
        heapq.heappush(heap, (nc, ne))


for r in res[1:]:
    if len(r) < k:
        print(-1)
    else:
        print(-r[0])

