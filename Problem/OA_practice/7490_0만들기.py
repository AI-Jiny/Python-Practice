import re

def calculator(str):
    str = str.replace(" ", "")
    token = re.split(r"([+-])", str)
    res = 0
    state = 1
    for to in token:
        if to == "+":
            state = 1
        elif to == "-":
            state = -1
        else:
            to = int(to)
            res += state * to
    return res

def dfs(nums, idx, cur_str):
    if idx == n - 1:
        if not calculator(cur_str):
            ans.append(cur_str)
            return
    for s in ['+', '-', ' ']:
        if idx < n - 1:
            nxt_str = cur_str + s + str(nums[idx + 1])
            dfs(nums, idx + 1, nxt_str)

t = int(input())
total_ans = []
for ti in range(t):
    n = int(input())
    nums = [i for i in range(1, n + 1)]
    ans = []
    dfs(nums, 0, str(nums[0]))
    ans.sort()
    total_ans.extend(ans)
    if ti != t - 1:
        total_ans.append("")

for an in total_ans:
    print(an)