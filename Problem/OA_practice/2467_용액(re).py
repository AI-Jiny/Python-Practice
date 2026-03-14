n = int(input())
l = [int(x) for x in input().split()]
left = 0
right = n - 1
ans_sum = 2000000000
ans = (None, None)

while left < right:
    s = l[left] + l[right]
    if abs(s) < ans_sum:
        ans_sum = abs(s)
        ans = (l[left], l[right])
   
    if s < 0:
        left += 1
    elif s == 0:
        break
    else:
        right -= 1    
print(ans[0], ans[1])

# 4
# -100 -2 -1 103