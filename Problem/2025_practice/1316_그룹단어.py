n = int(input())
words = []
for _ in range(n):
    words.append(input())

ans = 0

for word in words:
    cur = None
    is_ok = True
    wset = set()
    for w in word:
        if w != cur:
            if w in wset:
                is_ok = False
                break
            wset.add(w)
            cur = w
    if is_ok:
        ans += 1

print(ans)