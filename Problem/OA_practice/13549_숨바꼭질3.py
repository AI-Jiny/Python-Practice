from collections import deque
from math import inf

N, K = [int(x) for x in input().split()]
size = max(N, K) * 2
dist = [inf] * size

def dfs(start, end):
    dq = deque([])
    dq.append(start)
    dist[start] = 0
    while dq:
        x = dq.popleft()

        if x == end:
            return dist[K]
        
        if x and (nx := x * 2) < size:
            dq.appendleft(nx)
            dist[nx] = dist[x]
        
        for nx in (x - 1, x + 1):
            if 0<= nx < size and dist[nx] > dist[x] + 1:
                dq.append(nx)
                dist[nx] = dist[x] + 1


print(dfs(N, K))
 