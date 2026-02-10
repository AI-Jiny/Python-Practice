N, M = map(int, input().split())
list_n = sorted([int(x) for x in input().split()])
path = []
idx_chk = []
dict_check = {}

def dfs(start):
    k = ",".join([str(x) for x in path])
    if len(path) == M and k not in dict_check:
        print(*path)
        dict_check[k] = True
        return
    
    for i in range(N):
        if i in idx_chk:
            continue
        path.append(list_n[i])
        idx_chk.append(i)
        dfs(i + 1)
        path.pop()
        idx_chk.pop()


dfs(0)
print(list_n)
print(dict_check)