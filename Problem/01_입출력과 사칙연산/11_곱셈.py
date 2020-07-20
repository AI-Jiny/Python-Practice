a = int(input())
b = str(input())
for i in range(2, -1, -1):
    print(a * int(b[i]))
print(a * int(b))
