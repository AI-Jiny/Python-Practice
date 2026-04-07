import heapq

N = int(input())
heap = [-10e9] * N

for _ in range(N):
    nums = [int(x) for x in input().split()]
    for num in nums:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

ans = heapq.heappop(heap)
print(ans)

# 5
# 12 7 9 15 5
# 13 8 11 19 6
# 21 10 26 31 16
# 48 14 28 35 25
# 52 20 32 41 49


# 100 7 9 15 1
# 101 8 11 19 2
# 102 10 26 31 3
# 103 14 28 35 4
# 104 20 32 41 5
