N, S, P = map(int, input().split())
ans = 1
tmp = None
if N:
    ans = -1
    ranking = [int(x) for x in input().split()]
    buffer = P - len(ranking)
    if buffer > 0:
        ranking += [-1] * buffer
        
    for i, r in enumerate(ranking[:P]):
        if r < S:
            ans = tmp if tmp else i + 1
            break
        elif r == S and not tmp:
            tmp = i + 1

print(ans)

# 3 90 10
# 100 90 80
# 2

# 10 1 10
# 10 9 8 7 6 5 4 3 2 1
# -1

# 10 1 10
# 10 9 8 7 6 5 4 3 3 0
# 10