N, M = map(int, input().split())
list_n = sorted([int(x) for x in input().split()])
path = []

def dfs(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        if list_n[i] in path:
            continue
        path.append(list_n[i])
        dfs(i + 1)
        path.pop()

dfs(0)