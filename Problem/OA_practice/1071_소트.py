N = int(input())
list_n = sorted([int(x) for x in input().split()])
dict_n = {}
for n in list_n:
    dict_n[n] = dict_n.get(n, 0) + 1

list_remain = sorted([int(x) for x in dict_n.keys()], reverse= True)
list_answer = []

last_n = -2
for _ in range(N):
    idx = -1
    
    if last_n + 1 == list_remain[idx]:
        idx -= 1
    elif len(list_remain) == 2 and list_remain[-1] + 1 == list_remain[-2]:
        idx -= 1
    
    list_answer.append(str(list_remain[idx]))
    last_n = list_remain[idx]
    dict_n[list_remain[idx]] -= 1
    if not dict_n[list_remain[idx]]:
        list_remain.pop(idx)

print(" ".join(list_answer))