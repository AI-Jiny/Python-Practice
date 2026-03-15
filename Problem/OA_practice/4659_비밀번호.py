ans = []

while True:
    word = input()
    if word == 'end':
        break
    mo = ['a', 'e', 'i', 'o', 'u']
    is_ok = True
    flg = True

    for m in mo:
        if m in word:
            flg = False
    
    three_cnt = 0
    last = None
    for i in range(len(word)):
        if word[i] == last and word[i] not in ['e', 'o']:
            is_ok = False
            break
        if (last in mo and word[i] in mo) or (last not in mo and word[i] not in mo):
            three_cnt += 1
        else:
            three_cnt = 1
        
        if flg or three_cnt == 3:
            is_ok = False
            break
        last = word[i]
    
    if is_ok:
        ans.append(f"<{word}> is acceptable.")
    else:
        ans.append(f"<{word}> is not acceptable.")

for an in ans:
    print(an)