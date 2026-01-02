N = int(input())
list_n = [int(x) for x in input().split()]
list_rank = sorted(list(set(list_n)))
dict_rank = {}
for i, n in enumerate(list_rank):
    dict_rank[n] = i

ans = 0

size = 1
while size < len(list_rank):
    size <<= 1
tree = [0] * 2 * size

def update(idx, value = 1):
    pos = idx + size
    while pos:
        tree[pos] += value
        pos //= 2

def search(left, right):
    left += size
    right += size
    res = 0

    while left <= right:
        if left & 1:
            res += tree[left]
            left += 1
        if not(right & 1):
             res += tree[right]
             right -= 1
        left //= 2
        right //= 2
    return res

for n in list_n:
    ans += search(dict_rank[n]+1, len(list_rank) - 1)
    update(dict_rank[n])

print(ans)
