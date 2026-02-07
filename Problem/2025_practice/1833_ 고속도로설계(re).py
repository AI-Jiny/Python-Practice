n = int(input())
parents = [int(i) for i in range(n)]
graph = []
ans = 0
ans_list = []

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
        parents[pb] = parents[pa]
    else:
        parents[pa] = parents[pb]


for s in range(n):
    costs = [int(x) for x in input().split()]
    for e in range(s + 1, n):
        c = costs[e]
        
        if c < 0:
            union(parents, s, e)
            ans -= c
        elif c > 0:
            graph.append((c, s, e))

graph.sort()

for g in graph:
    c, s, e = g
    if find(parents, s) != find(parents, e):
        union(parents, s, e)
        ans += c
        ans_list.append((s + 1, e + 1))

print(ans, len(ans_list))
for an in ans_list:
    s, e = an
    print(s, e)




# 5
#    0  -10 1000  -20 1000
#  -10    0   10  -30 1000
# 1000   10    0   30   10
#  -20  -30   30    0   20
# 1000 1000   10   20    0