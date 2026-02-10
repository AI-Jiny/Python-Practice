import math
n = int(input())
squares = [i**2 for i in range(1, int(math.isqrt(n)) + 1)]
dp = [0] + [4] * n

for i in range(1, n + 1):
    for sq in squares:
        if sq > i:
            break
        dp[i] = min(dp[i], dp[i - sq] + 1)

print(dp[n])   

"""
34567
11339
1 : 1           = 1
2 : 1 + 1       = 2
3 : 1 + 1 + 1   = 3
4 : 2           = 4
5 : 2 + 1       = 2
6 : 
"""
