a=input()

def mul(a):
    num = 1
    a = a.split(" ")
    a = list(map(int, a))
    for i in a:
        num = num * i
    
    return num

print(mul(a))

