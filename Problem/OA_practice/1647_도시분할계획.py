import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [int(i) for i in range(n + 1)]
graph = []

def find(parents, node):
    p = node
    while p != parents[p]:
        p = parents[p]
    
    curr = node
    while curr != p:
        nxt = parents[curr]
        parents[curr] = p
        curr = nxt
    return p

def union(parents, a, b):
    pa = find(parents, a)
    pb = find(parents, b)

    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb

for _ in range(m):
    s, e, c = map(int, input().split())
    graph.append((c, s, e))

graph.sort()

total_cost = 0
top_cost = 0

for g in graph:
    c, s, e = g
    if find(parents, s) != find(parents, e):
        union(parents, s, e)
        total_cost += c
        if top_cost < c:
            top_cost = c

ans = total_cost - top_cost
print(ans)