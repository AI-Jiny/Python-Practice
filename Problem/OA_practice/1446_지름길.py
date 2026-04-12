N, D = map(int, input().split())
dp = [i for i in range(D + 1)]
roads = []

for _ in range(N):
    s, e, d = map(int, input().split())
    roads.append((s, e, d))

roads.sort()
for road in roads:
    s, e, d = road
    if D < e:
        continue
    dd = dp[s] + d
    for i in range(e, D + 1):
        dp[i] = min(dp[i], dd + i - e)

print(dp[D])

# 5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90