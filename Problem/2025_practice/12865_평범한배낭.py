N, k = [int(x) for x in input().split()]
list_n = [[int(w), int(v)] for w, v in (input().split() for _ in range(N))]
list_n.sort(key=lambda x: x[0] / x[1])
answer = 0
print(list_n)
for w, v in list_n:
    if w <= k:
        answer += v
        k -= w

print(answer)
