n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        pre = 0 if j == 0 else dp[i - 1][j - 1]
        nxt = 0 if j == 9 else dp[i - 1][j + 1]
        dp[i][j] = (pre + nxt) % 1000000000

print((sum(dp[n]) % 1000000000))