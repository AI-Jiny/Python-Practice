N, K = map(int, input().split())
nums = [int(x) for x in input().split()]
num_dict = {}
left = 0
right = 0
ans = 0

while right <= N - 1:
    lnum = nums[left]
    rnum = nums[right]
    v = num_dict.get(rnum, 0)

    if v + 1 > K:
        num_dict[lnum] -= 1
        left += 1
    else:
        num_dict[rnum] = v + 1
        right += 1

    if (nans := (right - left)) > ans:
        ans = nans

print(ans)