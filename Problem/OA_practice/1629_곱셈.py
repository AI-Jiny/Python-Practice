A, B, C = [int(x) for x in input().split()]
b = B
size = 1
remain = A % C
ans = 1 if size < B else remain
while size < B:
    if b % 2 == 1:
        b = (b - 1) // 2
        ans = (ans * remain) % C
    else:
        b //= 2

    remain = (remain ** 2) % C

    size <<= 1

print(ans)