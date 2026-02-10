n, k = [int(x) for x in input().split()]
ordered_list = []

size = 1
while size < n:
    size <<= 1
tree = [0] * (2 * size)

for i in range(size, size + n):
    tree[i] = 1

for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

def update(idx, value = 1):
    pos = idx + size
    while pos:
        tree[pos] -= value
        pos //= 2

def query(left, right):
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

pos = 0

while all_total := tree[1]:
    count = None
    if k > tree[1]:
        count = c if (c := k % tree[1]) else all_total
    else:
        count = k
    
    if (gap := query(pos, n - 1)) < count:
        count -= gap
        pos = 0
    left_total = all_total - query(pos, n - 1)
    target_count = left_total + count

    target_idx = 1
    while target_idx < size:
        if tree[target_idx * 2] < target_count:
            target_count -= tree[target_idx * 2]
            target_idx = target_idx * 2 + 1
        else:
            target_idx *= 2
    
    pos = target_idx - size
    update(pos)
    ordered_list.append(str(pos + 1))


answer = f"<{', '.join(ordered_list)}>"
print(answer)
    
        

