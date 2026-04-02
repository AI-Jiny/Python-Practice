import sys

input = sys.stdin.readline
N = int(input())
nums = []
ans = []
for _ in range(N):
    nums.append(int(input()))

heap = [0]
def push(node):
    heap.append(node)
    idx = len(heap) - 1
    while idx > 1:
        if (child := heap[idx]) < (parent := heap[idx // 2]):
            heap[idx], heap[idx // 2] = parent, child
            idx //= 2
        else:
            break
def pop():
    if len(heap) >= 2:
        ans.append(heap[1])
        la = heap.pop()
        
        if len(heap) == 1:
            return
        heap[1] = la
    else:
        ans.append(0)
        return
    
    idx = 1
    while idx <= (len(heap) - 1) // 2:
        nidx = idx
        if heap[nidx] > heap[idx * 2]:
            nidx = idx * 2
        if idx * 2 + 1 < len(heap) and heap[nidx] > heap[idx * 2 + 1]:
            nidx = idx * 2 + 1

        if nidx != idx:
            heap[idx], heap[nidx] = heap[nidx], heap[idx]
            idx = nidx
        else:
            break
            

for num in nums:
    if num:
        push(num)
    else:
        pop()

for an in ans:
    print(an)