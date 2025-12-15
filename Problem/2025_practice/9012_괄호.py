import queue

n = int(input())
list_b = [str(x) for x in [input() for _ in range(n)]]
answer_list = []

for b in list_b:
    tmp_stack = []
    flag = True
    for s in b:
        if tmp_stack and tmp_stack[-1] != s:
            tmp_stack.pop()
        elif not tmp_stack and s == ')':
            flag = False
            break
        else:
            tmp_stack.append(s)

    if tmp_stack or not flag:
        answer_list.append("NO")
    else:
        answer_list.append("YES")

for ans in answer_list:
    print(ans)