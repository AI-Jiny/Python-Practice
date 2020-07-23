a = int(input())
for i in range(a * 2 - 1):
    print((-abs(i - a + 1) + a) * "*")