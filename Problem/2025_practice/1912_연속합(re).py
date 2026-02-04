n = int(input())
nums = [int(x) for x in input().split()]
prefix = [0] * (n + 1)
prefix[1] = nums[0]
ans = -1001
tmp = 1001

for i, num in enumerate(nums):
    prefix[i + 1] = prefix[i] + num

for p in prefix:
    if n == 1:
        ans = p
    elif ans < (nans := (p - tmp)):
        ans = nans

    if p < tmp:
        tmp = p

print(ans)