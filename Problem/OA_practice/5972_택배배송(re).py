import sys
from math import inf
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i: [] for i in range(n + 1)}
dp = [inf] * (n + 1)
dp[1] = 0
hq = []
heapq.heappush(hq, (0, 1))

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
    graph[e].append((c, s))

while hq:
    cost, cur = heapq.heappop(hq)
    if cost > dp[cur]:
        continue
    
    for g in graph[cur]:
        tc, nxt = g
        ncost = tc + cost
        if ncost < dp[nxt]:
            dp[nxt] = ncost
            heapq.heappush(hq, (ncost, nxt))

print(dp[-1])

# 6 8
# 4 5 3
# 2 4 0
# 4 1 4
# 2 1 1
# 5 6 1
# 3 6 2
# 3 2 6
# 3 4 4