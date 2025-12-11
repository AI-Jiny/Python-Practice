#n, k = [int(x) for x in input().split()]
#arr = list(range(1, n+1))
arr = [1] * 7
N = len(arr)
ordered_list = []

size = 1
while size < N:
    size <<= 1
tree = [0] * (2 * size)
#size -= 1

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

print(query(2, 5))

    
    
    