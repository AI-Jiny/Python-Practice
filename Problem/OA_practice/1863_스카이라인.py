N = int(input())
groups = []
ans = 0

for _ in range(N):
    w, h = map(int, input().split())
    while groups and groups[-1] > h:
        groups.pop()
    if h > 0 and (not groups or groups[-1] != h):
        ans += 1
        groups.append(h)

print(ans)

# 10
# 1 1
# 2 2
# 5 1
# 6 3
# 8 1
# 11 0
# 15 2
# 17 3
# 20 2
# 22 1