n = 1
for i in range(3):
    n = n * int(input())
n = list(str(n))
for j in range(10):
    print(n.count(str(j)))