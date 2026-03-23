N = int(input())
budgets = [int(x) for x in input().split()]
limit = int(input())

left = 0
right = max(budgets)
ans = 0

if sum(budgets) <= limit:
    ans = right
    left = right

while left < right:
    mid = (left + right) // 2

    print(left, mid, right)
    total = 0
    for b in budgets:
        if b > mid:
            total += mid
        else:
            total += b
    if total > limit:
        right = mid
    else:
        ans = mid
        left = mid + 1
    print(total)
print(ans)

# 4
# 120 110 140 150
# 485