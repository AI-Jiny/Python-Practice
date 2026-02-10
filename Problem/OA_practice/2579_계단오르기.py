n = int(input())
stairs = [0] * 301
for i in range(n):
    stairs[i] = int(input())


dp = [0] * 301
dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]
dp[2] = max(stairs[0], stairs[1]) + stairs[2]


for i, stair in enumerate(stairs[3:], 3):
    if not stairs[i]:
        break
    dp[i] = max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i]

print(dp[n -1])

