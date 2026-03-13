n, k = map(int,input().split())
countries = []
target = 0

for _ in range(n):
    idx, g, s, b = map(int,input().split())
    countries.append([(g, s, b), idx])
    if k == idx:
        target = (g, s, b)

countries.sort(reverse=True)

for i in range(n):
    s, idx = countries[i]
    if s == target:
        print(i + 1)
        break