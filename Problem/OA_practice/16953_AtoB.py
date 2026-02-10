from collections import deque
A, B = [int(x) for x in input().split()]
dict_ans = {A: 0}
dq = deque([A])

while dq:
    n = dq.popleft()
    if n == B:
        break

    if (nx1 := n * 2) <= B:
        dict_ans[nx1] = dict_ans[n] + 1
        dq.append(nx1)
    if (nx2 := int(str(n) + "1")) <= B:
        dict_ans[nx2] = dict_ans[n] + 1
        dq.append(nx2)

ans = dict_ans.get(B)
ans = ans + 1 if ans else -1
print(ans)
        