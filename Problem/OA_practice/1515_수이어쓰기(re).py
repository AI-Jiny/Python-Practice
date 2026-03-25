n = input()
idx = 0
cur_num = 0

while idx < len(n):
    cur_num += 1
    for char in str(cur_num):
        if char == n[idx]:
            idx += 1
            print(cur_num, idx, len(n))
        print(idx == len(n))
        if idx == len(n):
            break
print(cur_num)

# 1111111
# 999909