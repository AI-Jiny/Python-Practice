n = int(input())
a, b = [x for x in (input().split() for _ in range(2))]
a = " " + "".join(a)
b = " " + "".join(b)
la = len(a)
lb = len(b)
l_chk = [[0] * la for _ in range(lb)]
ans = []

for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            l_chk[j][i] = l_chk[j - 1][i - 1] + 1
        else:
            l_chk[j][i] = max(l_chk[j - 1][i], l_chk[j][i - 1])
        
idx_a = la - 1
idx_b = lb - 1

while idx_a > 0 and idx_b > 0:
    pidx_a = idx_a - 1
    pidx_b = idx_b - 1


    if a[idx_a] == b[idx_b]:
        ans.append(a[idx_a])
        idx_a -= 1
        idx_b -= 1
    else:
        if l_chk[pidx_b][idx_a] < l_chk[idx_b][pidx_a]:
            idx_a -= 1
        else:
            idx_b -= 1
    

print(l_chk[lb - 1][la - 1])
print("".join(ans[-1::-1]))