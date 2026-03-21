N = int(input())
M = int(input())
lamps = [int(x) for x in input().split()]

left = lamps[0]
right = N - lamps[-1]
diff = 0
for i in range(1, M):
    diff = max(lamps[i] - lamps[i - 1], diff)
diff = (diff + 1) // 2

ans = max(left, right, diff)
print(ans)