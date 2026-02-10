n, r, c = [int(x) for x in input().split()]
list_cnt = [[0,1],[2,3]]
ans = 0

def to_binary(x, n):
    bx = str(bin(x))[2:]
    c = n - len(bx)
    nx = ("0" * c) + bx
    return nx

br = to_binary(r, n)
bc = to_binary(c, n)

for i in range(n):
    idx_r = int(br[i])
    idx_c = int(bc[i])
    cnt = list_cnt[idx_r][idx_c]
    ans += cnt * (2 ** (2 * (n - i)- 2))
print(ans)

### 비트 인터리빙 정석 코드
# n, r, c = [int(x) for x in input().split()]
# ans = 0
# for i in range(n):
#     ans <<= 2
#     ans |= ((r >> (n-1-i)) & 1) << 1 | ((c >> (n-1-i)) & 1)
# print(ans)