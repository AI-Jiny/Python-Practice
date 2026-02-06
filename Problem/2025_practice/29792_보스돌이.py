import math

n, m, k = map(int, input().split())
characters = [int(input()) for _ in range(n)]
bosses = []
ans = 0

for _ in range(k):
    x, y = map(int, input().split())
    bosses.append((x, y))

characters.sort(reverse=True)
bosses.sort()
playable = characters[:m]


def dfs(damage, idx, time ,meso):
    boss = bosses[idx]
    if damage * time < boss[0]:
        return meso
    ntime = time - math.ceil(boss[0] / damage)
    nmeso = meso + boss[1]
    if idx < k - 1:
        res = max(dfs(damage, idx + 1, time, meso), dfs(damage, idx + 1, ntime, nmeso))
    else:
        res = nmeso
#    print(f"p:{damage}, boss:{boss}, ntime:{ntime}, nmeso: {nmeso},res: {res}")

    return res

for d in playable:
    ans += dfs(d, 0, 900, 0)

print(ans)