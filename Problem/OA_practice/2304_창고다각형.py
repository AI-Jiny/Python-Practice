N = int(input())
pillars = []
for _ in range(N):
    idx, height = map(int, input().split())
    pillars.append((idx, height))

pillars.sort()

print(pillars)
# 7
# 2 4
# 11 4
# 15 8
# 4 6
# 5 3
# 8 10
# 13 6