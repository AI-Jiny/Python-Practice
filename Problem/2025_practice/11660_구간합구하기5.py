N, M = [int(x) for x in input().split()]
list_map = [[int(x) for x in input().split()] for _ in range(N)]
list_q = [[int(x) for x in input().split()] for _ in range(M)]
list_presum = [[0] for i in range(N)]
list_presum2 = [[0] * (N + 1)]
for i, l in enumerate(list_map):
    for j, n in enumerate(l):
        list_presum[i].append(list_presum[i][-1] + n)

for i in range(1, N + 1):
    list_tmp = []
    for j in range(N + 1):
        list_tmp.append(list_presum2[i - 1][j] + list_presum[i - 1][j])
    list_presum2.append(list_tmp)


for q in list_q:
    x1, y1, x2, y2 = q
    ans = list_presum2[x2][y2] - (list_presum2[x1 - 1][y2] + list_presum2[x2][y1 - 1]) + list_presum2[x1 - 1][y1 - 1]
    
    print(ans)
    