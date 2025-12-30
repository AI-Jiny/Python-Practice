N, M = map(int, input().split())
path = []

def dfs(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        path.append(i)
        dfs(i + 1)
        path.pop()

dfs(1)