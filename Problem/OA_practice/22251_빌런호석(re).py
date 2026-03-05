n, k, p, x = map(int, input().split())
change_cnt = {i: [0] * 10 for i in range(10)}
nums = [0b1110111, 0b0010010, 0b1011101, 
        0b1011011, 0b0111010, 0b1101011,
        0b1101111, 0b1010010, 0b1111111,
        0b1111011]
ans = 0

for i in range(10):
    for j in range(10):
        if i == j:
            continue
        cnt = (nums[i] ^ nums[j]).bit_count()
        change_cnt[i][j] = cnt

target = str(x)
zero_need = k - len(target)
target = "0" * zero_need + target


def dfs(idx, p, cur_str):
    global ans

    if idx == len(target):
        if 1 <= (final_x := int(cur_str)) <= n and final_x != x:
            ans += 1
        return

    num = int(target[idx])
    cnt_list = change_cnt[num]
    for i, cnt in enumerate(cnt_list):
        nxt_str = cur_str + str(i)
        if cnt <= p:
            dfs(idx + 1, p - cnt, nxt_str)

dfs(0, p, "")

print(ans)