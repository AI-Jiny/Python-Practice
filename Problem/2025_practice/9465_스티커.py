T = int(input())
list_fans = []
for _ in range(T):
    n = int(input())
    ans = 0

    list_na = [0,0] + [int(x) for x in input().split()]
    list_nb = [0,0] + [int(x) for x in input().split()]
    list_ans = [[0,0], [0,0]]

    for i in range(2, n + 2):
        ans_a = max(list_ans[i -2][1], list_ans[i - 1][1]) + list_na[i]
        ans_b = max(list_ans[i -2][0], list_ans[i - 1][0]) + list_nb[i]
        ans = max(ans, ans_a, ans_b)
        list_ans.append([ans_a, ans_b])
    list_fans.append(ans)

for a in list_fans:
    print(a)
