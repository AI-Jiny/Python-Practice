n = int(input())
aas = [int(x) for x in input().split()]
bbs = [int(x) for x in input().split()]
ans = 0

aas.sort()
bbs.sort(reverse=True)

for a,b in zip(aas, bbs):
    ans += a * b

print(ans)