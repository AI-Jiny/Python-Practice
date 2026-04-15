from collections import deque

N, L, R = map(int, input().split())
countries = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0

for _ in range(N):
    row = [int(x) for x in input().split()]
    countries.append(row)

def bfs(r, c, visited):
    dq = deque([(r,c)])
    union = [(r,c)]
    union_sum = countries[r][c]
    visited[r][c] = True
    while dq:
        row,col = dq.popleft()
        
        for i in range(4):
            nr = row + dy[i]
            nc = col + dx[i]
            if 0 <= nr < N and 0 <= nc < N and L <= abs(countries[nr][nc] - countries[row][col]) <= R and not visited[nr][nc]:
                dq.append((nr,nc))
                union.append((nr, nc))
                union_sum += countries[nr][nc]
                visited[nr][nc] = True
    return union, union_sum

while True:
    visited = [[False] * N for _ in range(N)]
    is_moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, union_sum = bfs(i, j ,visited)
                union_avg = union_sum // len(union)

                if len(union) > 1:
                    is_moved = True
                    for un in union:
                        r, c = un
                        countries[r][c] = union_avg
    if is_moved:
        ans += 1
    else:
        break
print(ans)

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10
# 2

# 2 40 50
# 50 30
# 20 40
# 0