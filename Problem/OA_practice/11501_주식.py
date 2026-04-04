import sys

input = sys.stdin.readline
T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    prices = [int(x) for x in input().split()]
    max_price = 0
    total = 0
    for price in prices[-1::-1]:
        max_price = max(max_price, price)
        total += max_price - price
    ans.append(total)
for an in ans:
    print(an)
# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2