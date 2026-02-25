from collections import deque

n, m = map(int, input().split())
dp = [-1 for _ in range(101)]
teleport = {}
dq = deque([])

for _ in range(n + m):
    s, e = map(int, input().split())
    teleport[s] = e

dq.append((1, 0))
while dq:
    s, c = dq.popleft()

    for i in range(1, 7):
        ns = teleport.get(s + i, s + i)
        nc = c + 1
        if ns <= 100 and dp[ns] == -1:
            dp[ns] = nc
            dq.append((ns, nc))

print(dp[-1])