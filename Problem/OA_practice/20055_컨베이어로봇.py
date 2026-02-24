n, k = map(int, input().split())
belts = [int(x) for x in input().split()]
s, t = (0, n - 1)
robots = [False] * 2 * n
zb = 0
ans = 0

while zb < k:
    s = (s - 1) % (2 * n)
    t = (t - 1) % (2 * n)
    robots[t] = False
    for i in range(n):
        idx = (t - i) % (2 * n)
        nidx = (idx + 1) % (2 * n)
        if robots[idx] and not robots[nidx] and belts[nidx]:
            robots[idx] = False
            belts[nidx] -= 1
            if nidx != t:
                robots[nidx] = True
            if not belts[nidx]:
                zb += 1
    
    if belts[s]:
        robots[s] = True
        belts[s] -= 1
        if not belts[s]:
            zb += 1
    ans += 1

print(ans)
            
                
    