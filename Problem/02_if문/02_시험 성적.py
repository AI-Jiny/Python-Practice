a=input()
#a = a.split(" ")
#a = list(map(int, a))
a = int(a)
if a % 400 == 0 :
    print("1")
elif a % 100 == 0 :
    print("0")
elif a % 4 == 0 :
    print("1")
else:
    print("0")