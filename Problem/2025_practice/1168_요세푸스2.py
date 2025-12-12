n, k = [int(x) for x in input().split()]
arr = [1] * n
N = len(arr)
ordered_list = []

size = 1
while size < N:
    size <<= 1
tree = [0] * (2 * size)

for i, x in enumerate(arr):
    idx = size + i
    while idx:
        tree[idx] += x
        idx //= 2

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

def search_idx(src, target):
    left = src
    right = N - 1


    while left <= right:
        if tree[right + size] and query(src, right) == target:
            return right
        mid = (left + right) // 2

        #print(f"left: {left}, right: {right}, mid: {mid},value:{right+size}")

        if target <= query(src, mid) :
            right = mid
        else:
            left = mid + 1

pos = 0

while tree[1]:
    count = None
    if k > tree[1]:
        count = c if (c := k % tree[1]) else tree[1]
    else:
        count = k

    if (gap := query(pos, N)) < count:
        count -= gap
        pos = 0
    #print(f"people: {tree[1]}, pos:{pos},count: {count}")
    pos = search_idx(pos, count)
    #print(f"pos: {pos}")
    update(pos)
    ordered_list.append(str(pos + 1))
    #print(ordered_list)

answer = f"<{', '.join(ordered_list)}>"
print(answer)
    
        

