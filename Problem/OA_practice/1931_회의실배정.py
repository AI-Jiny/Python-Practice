N = int(input())
list_n = [[int(x),int(y)] for x,y in (input().split() for _ in range(N))]
list_n.sort(key=lambda x:(x[1], x[0]))
ans = 0
t = 0

for n in list_n:
    if n[0] >= t:
        ans += 1
        t = n[1]
print(ans)

    
    
