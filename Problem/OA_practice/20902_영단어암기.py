N, M = map(int, input().split())
notes = {}
ans = []

for _ in range(N):
    word = input()
    word_cnt = notes.get(word, 0)
    word_cnt += 1
    notes[word] = word_cnt

for k, v in notes.items():
    if len(k) >= M:
        ans.append(k)

ans.sort(key=lambda x: (-notes[x], -len(x), x))

for an in ans:
    print(an)

# 12 5
# appearance
# append
# attendance
# swim
# swift
# swift
# swift
# mouse
# wallet
# mouse
# ice
# age