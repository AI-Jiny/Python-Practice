import sys
from math import inf
import heapq

input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
K = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = [int(x) for x in input().split()]
    graph[s].append((c,e))

list_ans = [inf] * (N + 1)
heap = []
list_ans[K] = 0
heapq.heappush(heap, (0, K))

while heap:
    c, e = heapq.heappop(heap)

    if list_ans[e] < c:
        continue

    for c2, ne in graph[e]:
        nc = c + c2

        if nc < list_ans[ne]:
            list_ans[ne] = nc
            heapq.heappush(heap, (nc, ne))


for ans in list_ans[1:]:
    if ans == inf:
        print("INF")
    else:
        print(ans)