a, b = [x for x in (input() for _ in range(2))]
a = " " + a
b = " " + b
la = len(a)
lb = len(b)
l_chk = [[0] * la for _ in range(lb)]

for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            l_chk[j][i] = l_chk[j - 1][i - 1] + 1
        else:
            l_chk[j][i] = max(l_chk[j - 1][i], l_chk[j][i - 1])

print(l_chk[lb -1][la - 1])