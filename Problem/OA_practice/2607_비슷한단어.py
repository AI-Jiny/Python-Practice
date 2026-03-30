from collections import Counter
N = int(input())
raw = [input() for _ in range(N)]
first, words = raw[0], raw[1:]
fcount = Counter(first)
ans = 0

for word in words:
    if len(word) < len(first) - 1 or len(first) + 1 < len(word):
        continue
    
    is_break = False
    target = fcount
    wordcount = Counter(word)
    gap = {}
    combine = set(target.keys()).union(set(wordcount.keys()))

    for key in combine:
        count = target.get(key, 0) - wordcount.get(key, 0)
        if abs(count) >= 2:
            is_break = True
            break
        elif count:
            gap[key] = count

    if len(gap) > 2 or is_break:
        continue
    if abs(sum(gap.values())) < 2:
        ans += 1

print(ans)
