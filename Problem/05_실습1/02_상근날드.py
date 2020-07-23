a = [int(input()) for _ in range(5)]
print(min(a[:3]) + min(a[3:]) - 50)