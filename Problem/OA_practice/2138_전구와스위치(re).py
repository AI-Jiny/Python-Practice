N = int(input())
start = [True if int(x) else False for x in input()]
start_d = start[:]
start_d[0] ^= True
start_d[1] ^= True
ans_1 = 0
ans_2 = 1
end = [x == '1' for x in input()]

for i in range(1, N):
    if start[i - 1] != end[i - 1]:
        start[i - 1] ^= True
        start[i] ^= True
        if i + 1 < N:
            start[i + 1] ^= True
        ans_1 += 1
    if start_d[i - 1] != end[i - 1]:
        start_d[i - 1] ^= True
        start_d[i] ^= True
        if i + 1 < N:
            start_d[i + 1] ^= True
        ans_2 += 1

ans = []

if start[-1] == end[-1]:
    ans.append(ans_1)
if start_d[-1] == end[-1]:
    ans.append(ans_2)

if ans:
    print(min(ans))
else:
    print(-1)
    

