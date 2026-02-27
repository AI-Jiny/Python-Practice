n = int(input())
tops = [0] + [int(x) for x in input().split()]
lights = []
ans = [0] * (n + 1)

for i in range(n, 0, -1):
    s = tops[i]
    tmp = []
    while lights and lights[-1][0] < s:
        k, idx = lights.pop()
        ans[idx]= i
    lights.append((s,i))

print(" ".join(map(str, ans[1:])))