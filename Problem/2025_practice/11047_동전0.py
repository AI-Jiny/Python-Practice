n,k = map(int, input().split())
list_n = sorted([int(x) for x in (input() for _ in range(n))], reverse=True)
ans = 0

for n in list_n:
    t = k // n
    ans += t
    k -= t * n
print(ans)