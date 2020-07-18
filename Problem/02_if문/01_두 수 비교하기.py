a=input()
a = a.split(" ")
a = list(map(int, a))
if a[0] > a[1]:
    print(">")
elif a[0] < a[1]:
    print("<")
else:
    print("==")
