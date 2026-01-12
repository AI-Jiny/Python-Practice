N = int(input())
M = int(input())
s = input()
ans = 0
k = 0

idx = s.find("IOI")
#while idx != -1 and idx + 2 < M:
for _ in range(5):
    print(idx)
    if s[idx + 1: idx + 3] == "OI":
        k += 1
        idx += 2
    else:
        nidx = s[idx:].find("IOI")
        if nidx == -1:
            break
        idx += nidx
        k = 0

    if k >= N:
        ans += 1

print(ans)

