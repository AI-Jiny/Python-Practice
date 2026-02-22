n = int(input())
options = []
shortcut_keys = set()
ans = []

for _ in range(n):
    options.append(input())


for option in options:
    words = option.split()
    tmp = ""
    idx = 0
    for w in words:
        lower = w[0].lower()
        upper = w[0].upper()
        if lower in shortcut_keys or upper in shortcut_keys:
            idx += len(w) + 1
            continue
        else:
            tmp = w[0]
            break
    if not tmp:
        idx = 0
        for i, w in enumerate(option):
            if w == " ":
                continue
            lower = w.lower()
            upper = w.upper()
            if lower in shortcut_keys or upper in shortcut_keys:
                continue
            else:
                tmp = w
                idx = i
                break
    if tmp:
        
        roptions = list(option)
        roptions[idx] = f"[{tmp}]"
        option = "".join(roptions)
        shortcut_keys.add(tmp)
    ans.append(option)

for an in ans:
    print(an)

# 5
# New
# Open
# Save
# Save As
# Save All