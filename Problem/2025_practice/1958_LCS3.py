a, b, c = [x for x in (input() for _ in range(3))]
a = " " + a
b = " " + b
c = " " + c
la = len(a)
lb = len(b)
lc = len(c)
l_chk = [[[0] * la for _ in range(lb)] for _ in range(lc)]

for i in range(1, la):
    for j in range(1, lb):
        for k in range(1, lc):
            if a[i] == b[j] == c[k]:
                l_chk[k][j][i] = l_chk[k - 1][j - 1][i - 1] + 1
            else:
                l_chk[k][j][i] = max(l_chk[k - 1][j][i], l_chk[k][j - 1][i], l_chk[k][j][i - 1])

print(l_chk[lc - 1][lb - 1][la - 1])