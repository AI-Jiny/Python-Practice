a=input()

def total(a):
    a = a.split(" ")
    a = list(map(int, a))
    print(a[0] + a[1])
    print(a[0] - a[1])
    print(a[0] * a[1])
    print(a[0] // a[1])
    print(a[0] % a[1])
total(a)