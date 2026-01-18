N = int(input())
M = int(input())
s = input()
ans = 0
k = 0

idx = s.find("IOI")
while idx != -1 and idx + 2 < M:
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


## 정석 코드
# N = int(input())
# M = int(input())
# S = input()

# ans = 0
# cnt = 0  # 연속된 "OI" 개수

# i = 0
# while i < M - 2:
#     if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
#         cnt += 1
#         if cnt >= N:
#             ans += 1
#         i += 2          # 겹침 허용: 다음 'I'부터 계속 확인
#     else:
#         cnt = 0
#         i += 1

# print(ans)