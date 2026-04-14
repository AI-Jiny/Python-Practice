S = input()
a_cnt = S.count("a")
my_str = S + S[:a_cnt]
cur_cnt = my_str[:a_cnt].count("b")
ans = cur_cnt
if ans:
    for i in range(len(S)):
        if my_str[i] == "b":
            cur_cnt -= 1
        if my_str[i +  a_cnt] == "b":
            cur_cnt += 1
        if not cur_cnt:
            ans = 0
            break
        elif cur_cnt < ans:
            ans = cur_cnt
print(ans)

# abababababababa
# babababababab
# a b a
# a b
# 3
# aabbaaabaaba
# bbaaabaab
#bababaaaabbaaabbbbabbaaabababbaaabbbbbaabbaaababab

# abbbbab
# abaaaaaaaabaabababaabaaabbbabaabbababaababbbabbbaaaababaabbaaabaaabaaabab
