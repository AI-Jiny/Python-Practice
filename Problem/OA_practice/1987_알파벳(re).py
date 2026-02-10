R, C = [int(x) for x in input().split()]

list_map = [x for x in (input() for _ in range(R))]
ans = 0
dr = (1,-1,0,0)
dc = (0,0,1,-1)

def dfs(r,c, mask, depth):
    global ans
    ans = max(ans, depth)
    
    for xr,xc in zip(dr,dc):
        nr, nc = r + xr, c + xc
        if 0<= nr < R and 0<= nc < C:
            nbit = 1 << (ord(list_map[nr][nc]) - 65)
            if (nbit & mask) == 0:
                dfs(nr, nc, mask | nbit, depth + 1)


start_bit = 1 << (ord(list_map[0][0]) - 65)
dfs(0, 0, start_bit, 1)
print(ans)
