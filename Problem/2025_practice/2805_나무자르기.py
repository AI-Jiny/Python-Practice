n, m = [int(x) for x in input().split()]
list_trees = [int(x) for x in  input().split()]

def get_v(num):
    res = 0
    for tree in list_trees:
        if tree >= num:
            res += tree - num
    return res

left = 0
right = max(list_trees)
ans = None


while left < right:
    mid = (left + right) // 2
    v = get_v(mid)
    if v >= m:
        left = mid + 1
        ans = mid
    elif v < m:
        right = mid

print(ans)