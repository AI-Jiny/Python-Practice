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
    print(pa,pb)
    if pa < pb:
        parents[b] = parents[a]
    else:
        parents[a] = parents[b]


parents = [0,1,2,3,4]
union(parents, 0, 1)
print(parents)
union(parents, 1, 2)
print(parents)
union(parents, 2, 3)
print(parents)
union(parents, 3, 4)
print(parents)