N = int(input())
tree = [[int(x) for x in input().split()] for _ in range(N)]
ans = [[0 for _ in range(k)] for k in range(1, N + 1)]
ans[0][0] = tree[0][0]

for i, row in enumerate(tree[1:], 1):
    for j, t in enumerate(row):
        pj1, pj2 = (j - 1, j)
        p1 = 0 if pj1 < 0 else ans[i - 1][pj1]
        p2 = 0 if pj2 >= i else ans[i - 1][pj2]
        ans[i][j] = max(p1, p2) + tree[i][j]


print(max(ans[N -1]))
