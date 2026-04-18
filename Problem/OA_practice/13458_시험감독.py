N = int(input())
nums = [int(x) for x in input().split()]
B, C = map(int, input().split())
ans = 0

for num in nums:
    nn = 1 if num <= B else ((num - B - 1) // C) + 2
    ans += nn
print(ans)
