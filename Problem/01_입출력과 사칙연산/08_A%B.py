a=input()

def div(a):
    a = a.split(" ")
    a = list(map(int, a))
    num = a[0]
    for i in a[1:]:
        num /= i
    return num

print(div(a))