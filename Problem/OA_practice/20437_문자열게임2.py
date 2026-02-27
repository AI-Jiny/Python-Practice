t = int(input())
ans = []
for _ in range(t):
    word = input()
    num = int(input())
    alpha = {}
    res1 = 10000
    res2 = -1
    flg = True

    for i, w in enumerate(word):
        t = alpha.get(w, [])
        t.append(i)
        alpha[w] = t

    for k, v in alpha.items():
        l = len(v)
        if l < num:
            continue

        flg = False
        for i in range(l - num + 1):
            diff = v[i + num - 1] - v[i] + 1
            if diff < res1:
                res1 = diff
            if res2 < diff:
                res2 = diff

    if flg:
        ans.append(-1)
    else:
        ans.append(f"{res1} {res2}")

for an in ans:
    print(an)