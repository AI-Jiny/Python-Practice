N = int(input())
M = int(input())
S = input()

p = "IO" * N + "I"
lenp = len(p)
ans = 0
idx_left = 0
idx_right = lenp - 1

if lenp <= M:
    for i in range(M - idx_right):
        if S[idx_left:idx_right + 1] == p:
            ans += 1
        
        idx_left += 1
        idx_right += 1


print(ans)