t = int(input())
n_list = []
for _ in range(t):
    n_list.append(int(input()))

max_n = max(n_list)
dp = [0 for _ in range(max_n + 1)]
dp[0] = 1

for c in [1, 2, 3]:
    for i in range(c, max_n + 1):
        dp[i] += dp[i - c]

for n in n_list:
    print(dp[n])


