from math import inf
N, M = map(int, input().split())
maps = [[int(x) for x in input().split()] for _ in range(N)]
dp = [[[inf,inf,inf] for _ in range(M)] for _ in range(N)]
dy = [-1, 0, 1]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = maps[0][i]


for i in range(1, N):
    for j in range(M): 
        for d in range(3):
            pj = j + dy[d]
            if 0 <= pj < M:
                costs = [dp[i - 1][pj][pd] for pd in range(3) if pd != d]
                dp[i][j][d] = min(costs) + maps[i][j]

ans = min(val for row in dp[N -1] for val in row)
print(ans)