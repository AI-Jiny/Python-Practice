n = int(input())
graph = [0 for _ in range(501)]
dp = [1 for _ in range(501)]

for _ in range(n):
    s, e = map(int, input().split())
    graph[s] = e

for i in range(len(graph)):
    tmp = 0
    for j in range(i, -1, -1):
        if graph[j] < graph[i] and tmp < dp[j]:
            tmp = dp[j]
    dp[i] += tmp

ans = n - max(dp) + 1
print(ans)

# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6