import sys
input = sys.stdin.readline
res = 0

def find(parent, node):
    p = node
    while parent[p] != p:
        p = parent[p]
    
    curr = node
    while curr != p:
        nxt = parent[curr]
        parent[curr] = p
        curr = nxt
    return p

def union(parent, a, b):
    roota = find(parent, a)
    rootb = find(parent, b)

    if roota < rootb:
        parent[rootb] = parent[roota]
    else:
        parent[roota] = parent[rootb]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []

for _ in range(m):
    s, e, c = map(int,input().split())
    graph.append((c, s, e))

graph.sort()

for g in graph:
    c, s, e = g
    if find(parent, s) != find(parent, e):
        union(parent, s, e)
        res += c

print(res)


