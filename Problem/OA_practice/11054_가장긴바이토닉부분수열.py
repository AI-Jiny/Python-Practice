N = int(input())
list_n = [int(x) for x in input().split()]

list_left = [0 for _ in range(N)]
list_right = [0 for _ in range(N)]
ans = 0

for i, n in enumerate(list_n):
    res = 1
    for j in range(i):
        if list_n[j] < n and res <= list_left[j]:
            res = list_left[j] + 1
    list_left[i] = res

for i in range(N - 1, -1, -1):
    res = 1
    for j in range(i, N):
        if list_n[j] < list_n[i] and res <= list_right[j]:
            res = list_right[j] + 1
    list_right[i] = res

for i in range(N):
    s = list_left[i] + list_right[i] - 1
    ans = max(ans, s)

print(ans)
