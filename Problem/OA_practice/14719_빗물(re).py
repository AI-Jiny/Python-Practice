h, w = map(int, input().split())
blocks = [int(x) for x in input().split()]
ans = 0

for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])
    height = min(left, right)
    if blocks[i] < height:
        ans += height - blocks[i]

print(ans)

# 4 4
# 3 0 1 4

# 4 8
# 3 1 2 3 4 1 1 2
