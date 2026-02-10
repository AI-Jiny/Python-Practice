n = int(input())
list_n = [int(x) for x in input().split()]
list_ans = [1]
for i,n in enumerate(list_n[1:]):
    i += 1
    tmp = 1
    for j in range(i - 1,-1, -1):
        if list_n[j] < n and  tmp <= list_ans[j]:
            tmp = list_ans[j] +1
    
    list_ans.append(tmp)

print(max(list_ans))
