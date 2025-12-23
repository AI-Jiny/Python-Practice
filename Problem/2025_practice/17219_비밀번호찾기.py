N, M = [int(x) for x in input().split()]
list_n = sorted([[x, y] for x, y in (input().split() for _ in range(N))])
list_m = [x for x in (input() for _ in range(M))]
list_ans = []

for m in list_m:
    left = 0
    right = N - 1
    idx = None
    while left <= right:
        mid = (left + right) // 2
        # print(list_n[mid][0])
        # print(m)
        if list_n[mid][0] > m:
            right = mid
        elif list_n[mid][0] < m:
            left = mid + 1
        else:
            idx = mid
            break
    print(list_n[idx][1])
