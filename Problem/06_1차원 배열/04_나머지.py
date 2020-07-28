a = [int(input()) for _ in range(10)]
for i in range(10):
    a[i] = a[i] % 42
b = list(set(a))
print(len(b))