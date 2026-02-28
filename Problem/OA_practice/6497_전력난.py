import sys

input = sys.stdin.readline
ans = []

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


while True:
    finput = input()
    if not finput:
        break
    m, n = map(int, finput.split())
    
    if m == 0 and n == 0:
        break

    parents = [int(i) for i in range(m)]
    graph = []
    total = 0
    cost = 0


    for _ in range(n):
        s, e, c = map(int, input().split())
        total += c
        graph.append((c, s, e))



    graph.sort()

    for g in graph:
        c, s, e = g
        if find(parents, s) != find(parents, e):
            union(parents, s, e)
            cost += c

    res = total - cost
    ans.append(res)

for an in ans:
    print(an)
