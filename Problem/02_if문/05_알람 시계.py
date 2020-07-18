a = input()
a = a.split()
a = list(map(int, a))

if a[1] >= 45:
    print(a[0], a[1]-45)
elif a[0] == 0 and a[1] <45:
    print(23, a[1]+15)
else:
    print(a[0]-1, a[1]+15)