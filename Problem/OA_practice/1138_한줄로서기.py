from collections import Counter

N = int(input())
mask = 0
nums = [int(x) for x in input().split()]
ans = [0] * N

for i, num in enumerate(nums, 1):
    idx = 0
    for j in range(N):
        zero_count = Counter(ans[:j + 1]).get(0, 0)
        if zero_count == num + 1:
            ans[j] = str(i)
            break

print(" ".join(ans))


# 역순 방식 - O(N^2)
# N = int(input())
# nums = list(map(int, input().split()))
# ans = []

# # 키가 가장 큰 사람(N-1 인덱스)부터 역순으로 처리
# for i in range(N - 1, -1, -1):
#     # nums[i] 값 자체가 자신이 들어가야 할 정확한 인덱스가 됨
#     ans.insert(nums[i], str(i + 1))

# print(" ".join(ans))

 
# 4
# 2 1 1 0