R, C = [int(x) for x in input().split()]

list_map = [x for x in (input() for _ in range(R))]
visited_char = ""
set_path = set()
idx = (0,0,"0")
stack  = [idx]
ans = 0
tmp = ""
while stack:
    idx_r, idx_c, arrow = stack.pop()
    current_char = list_map[idx_r][idx_c]
    visited_char += current_char
    tmp += arrow
    is_end = True

    if idx_r + 1 < R and list_map[idx_r + 1][idx_c] not in visited_char and tmp + "1" not in set_path:
        stack.append((idx_r + 1, idx_c, "1"))
        is_end = False
    
    if idx_r - 1 >= 0 and list_map[idx_r - 1][idx_c] not in visited_char and tmp + "2" not in set_path:
        stack.append((idx_r - 1, idx_c, "2"))
        is_end = False

    if idx_c + 1 < C and list_map[idx_r][idx_c + 1] not in visited_char and tmp + "3" not in set_path:
        stack.append((idx_r, idx_c + 1, "3"))
        is_end = False

    if idx_c - 1 >= 0 and list_map[idx_r][idx_c - 1] not in visited_char and tmp + "4" not in set_path:
        stack.append((idx_r, idx_c - 1, "4"))
        is_end = False

    if is_end:
        set_path.add(tmp)
        ans = max(ans, len(tmp))
        tmp = tmp[:-1]
        visited_char = visited_char[:-1]
        set_path.discard(current_char)

    print(tmp)
    print(current_char)
    print(set_path)
    print(visited_char)
    print(stack)
    print("***************")

print(ans)

