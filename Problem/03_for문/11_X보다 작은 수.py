a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in b:
    if i < a[1]:
        c.append(str(i))
c = " ".join(c)
print(c)