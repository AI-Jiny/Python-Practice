n = int(input())
nums = [0]
flg = True

for i in range(n):
    nums.append(int(input()))

while True:
    flg = True
    for i, num in enumerate(nums[1:], 1):
        if nums[i] and i not in nums:
            nums[i] = 0
            flg = False
    if flg:
        break

nums.sort()
ans = set(nums)
ans.remove(0)
print(len(ans))
for an in ans:
    print(an)