a = int(input())
b = list(map(int, input().split()))
b = sorted(b)
print(str(b[0]) + " " + str(b[a-1]))