import sys
input = sys.stdin.readline

n = int(input())
graph =[]
s_graph = []
dp = [[1 for _ in range(n)] for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
ans = 0

for i in range(n):
    row = [int(x) for x in input().split()]
    graph.append(row)
    
    for j, c in enumerate(row):
        s_graph.append((c, i, j))

s_graph.sort(reverse=True)

for g in s_graph:
    c, i, j = g
    tmp = dp[i][j]
    for tr, tc in zip(dr,dc):
        ni = i + tr
        nj = j + tc
        if 0 <= ni < n and 0 <= nj < n and c < graph[ni][nj]:
            if tmp < dp[ni][nj] + 1:
                tmp = dp[ni][nj] + 1
    dp[i][j] = tmp
    if ans < tmp:
        ans = tmp

print(ans)

# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8