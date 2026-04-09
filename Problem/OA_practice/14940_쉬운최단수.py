import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = []


dp = [[-1 for _ in range(M)] for _ in range(N)]
dq = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    row = [int(x) for x in input().split()]
    board.append(row)

    for j in range(M):
        if row[j] == 2:
            dq.append((i, j))
            dp[i][j] = 0
        elif row[j] == 0:
            dp[i][j] = 0

while dq:
    i, j = dq.popleft()
    for v in range(4):
        ni = i + dx[v]
        nj = j + dy[v]
        if 0 <= ni < N and 0 <= nj < M and dp[ni][nj] == -1 and board[ni][nj]:
            dp[ni][nj] = dp[i][j] + 1
            dq.append((ni,nj))

for a in dp:
    print(" ".join(map(str, a)))


# 15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

