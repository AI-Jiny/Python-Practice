a = str(input())
b = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")
num = 0
for i in b:
    num += a.count(str(i))
print(len(a) - num)