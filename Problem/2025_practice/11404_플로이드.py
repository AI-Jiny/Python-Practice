import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    s, e, c = map(int,input().split())
    if c < graph[s][e]:
        graph[s][e] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (nr := (graph[i][k] + graph[k][j])) < graph[i][j]:
                graph[i][j] = nr

for g in graph[1:]:
    for i, n in enumerate(g):
        if n == inf:
            g[i] = 0
    ans = " ".join(map(str, g[1:]))
    print(ans)