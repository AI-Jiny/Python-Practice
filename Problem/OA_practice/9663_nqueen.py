n = int(input())
ans = 0
stack = []
chk_j = [0] * n
chk_cross = [0] * 2 * n
chk_rcross = [0] * 2 * n

def is_ok(i,j):
    if chk_j[j] or chk_cross[i + j] or chk_rcross[(i - j) + n]:
        return False
    else:
        return True

def bt(i):
    global ans
    if i >= n:
        return
    for j in range(n):
        if is_ok(i,j):
            stack.append((i,j))
            chk_j[j] = 1
            chk_cross[i + j] = 1
            chk_rcross[(i - j) + n] = 1
            if len(stack) == n:
                ans += 1
            bt(i + 1)
            stack.pop()
            chk_j[j] = 0
            chk_cross[i + j] = 0
            chk_rcross[(i - j) + n] = 0

bt(0)
print(ans)
