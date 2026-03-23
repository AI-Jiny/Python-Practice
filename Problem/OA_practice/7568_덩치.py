n = int(input())
humans = []
rank = 1
ans = [0] * n
for i in range(n):
    w, h  = [int(x) for x in input().split()]
    humans.append((w, h))


for i in range(n):
    w, h = humans[i]
    rank = 1
    for j in range(n):
        if i == j:
            continue
        w2, h2 = humans[j]
        if w < w2 and h < h2:
            rank += 1
    
    ans[i] = rank

ans = " ".join([str(x) for x in ans])
print(ans)