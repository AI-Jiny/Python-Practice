a = int(input())
for i in range(2*a- 1):
    print(((-abs(i-a + 1) + a-1) * " " + (abs(2*a-2-2*i) + 1) * "*"))