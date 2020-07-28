a = int(input())
b = list(map(int, input().split()))
c = max(b)
for i in range(a):
        b[i] = (b[i] / c) * 100
print(sum(b) / a)
