import sys
input = sys.stdin.readline

t = int(input())
ans = []
def get_time(node):

    if dp[node] != -1:
        return dp[node]
        
    parents = d_dict[node]
    tmp = 0
    for p in parents:
        if tmp < (pt := get_time(p)):
            tmp = pt
    
    res = tmp + d_list[node]
    dp[node] = res
    return res


for _ in range(t):
    n, k = map(int, input().split())
    d_list = [0] + [int(x) for x in input().split()]
    d_dict = {i:[] for i in range(1, n + 1)}
    dp = [-1 for _ in range(n + 1)]
    for _ in range(k):
        s, e = map(int, input().split())
        d_dict[e].append(s)
    target = int(input())
    ans.append(get_time(target))

for a in ans:
    print(a)
# 2
# 4 4
# 10 1 100 10
# 1 2
# 1 3
# 2 4
# 3 4
# 4
# 8 8
# 10 20 1 5 8 7 1 43
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 5 7
# 6 7
# 7 8
# 7