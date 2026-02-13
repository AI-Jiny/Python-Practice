n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != 10001:
            nums = min(dp[i], dp[i - coin] + 1)
            dp[i] = nums
    
if dp[k] == 10001:
    ans = -1
else:
    ans = dp[k]
print(ans)