import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n = map(int,input().split())
graph = []
for _ in range(m):
    r = [int(x) for x in input().split()]
    graph.append(r)

dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    res = 0
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < m and 0 <= b < n and graph[x][y] < graph[a][b]:
            res += dfs(a, b)
    dp[x][y] = res
    return res
    
dfs(m - 1, n - 1)

print(dp[m - 1][n - 1])