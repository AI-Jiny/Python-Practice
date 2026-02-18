n = int(input())
p_list = map(int, input().split())
dp = [0 for _ in range(n + 1)]
for i, p in enumerate(p_list, 1):
    for j in range(i, n + 1):
        dp[j] = max(dp[j], dp[j - i] + p)

print(dp[-1])
# 10
# 1 1 2 3 5 8 13 21 34 55