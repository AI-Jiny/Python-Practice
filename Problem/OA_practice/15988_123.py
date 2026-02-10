T = int(input())
list_q = [int(x) for x in (input() for _ in range(T))]
max_q = max(list_q)
list_ans = [0] * (max_q + 1)
list_ans[0] = 1

list_ans[1] = 1
list_ans[2] = 2

for i in range(3, len(list_ans)):
    list_ans[i] = (list_ans[i -1] + list_ans[i -2] + list_ans[i -3]) % 1000000009

for q in list_q:
    print(list_ans[q])