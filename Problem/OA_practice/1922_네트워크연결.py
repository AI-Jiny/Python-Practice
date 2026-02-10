import sys

n = int(input())
m = int(input())
graph = []
parent = [i for i in range(n + 1)] 
ans = 0

def find(parent, node):
    p = node
    while parent[p] != p:
        p = parent[p]
    
    cur = node
    while cur != p:
        parent[cur] = p
        cur = parent[cur]
    
    return p

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = parent[rootA]
    else:
        parent[rootA] = parent[rootB]


for _ in range(m):
    s, e, c = map(int, input().split())
    graph.append((c, s, e))

graph.sort()

for g in graph:
    c, s, e = g
    if find(parent, s) != find(parent, e):
        union(parent, s, e)
        ans += c

print(ans)

