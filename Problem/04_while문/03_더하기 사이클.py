a = int(input())
n = 0
b = (a,)
while True:
    if n >= 1 and a == b[0]:
        break
    elif a < 10:
        a *= 11
        n += 1
    elif a >= 10:
        a = (a % 10) * 10 + (a // 10 + a % 10) % 10
        n += 1
print(n)
