temp = []
for _ in range(5):
    temp.append(int(input()))
    if 0 <= temp[_] < 40:
        temp[_] = 40
    else:
        pass
a = 0
for i in temp:
    a = a + i
print(int(a/5))