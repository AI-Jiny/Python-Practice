import math

n, k = map(int, input().split())
ans = math.comb(n + k -1, n) % 1000000000

print(ans)