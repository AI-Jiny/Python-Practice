a=input()
def sub(a):
    a = a.split(" ")
    num = int(a[0])
    num = num - int(a[1])
    return num

print(sub(a))