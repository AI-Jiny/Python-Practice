N = int(input())
for i in range(N):
    a = input()
    a = a.split(" ")
    a = list(map(int, a))
    print("Case #{}: {} + {} = {}".format(i+1, a[0], a[1], a[0]+a[1]))
