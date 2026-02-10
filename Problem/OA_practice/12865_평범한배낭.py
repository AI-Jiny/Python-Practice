N, k = [int(x) for x in input().split()]
list_n = [[int(w), int(v)] for w, v in (input().split() for _ in range(N))]
#list_n.sort(key=lambda x: (-x[0], x[1] / x[0]))
answer = 0
dict_v = {}

def get_v(idx, w):
    if (idx, w) in dict_v:
        return dict_v[(idx, w)]
    
    elif w - list_n[idx][0] >= 0: 
        if idx == N - 1:
            value = list_n[idx][1]
        else:
            value = max(get_v(idx + 1, w), get_v(idx + 1, w - list_n[idx][0]) + list_n[idx][1])
    else:
        if idx == N - 1:
            value = 0
        else:
            value = get_v(idx + 1, w)

    dict_v[(idx, w)] = value
    return value

print(get_v(0, k))


### 바텀업 방식 ### >> 대부분의 경우 바텀업이 나은 듯

# n, k = [int(x) for x in input().split()]

# dp = [0] * (k + 1)  # dp[w] = 무게 한도 w에서 가능한 최대 가치

# for _ in range(n):
#     w, v = map(int, input().split())

#     # 0/1 배낭이므로 "역순"으로 갱신해야 같은 물건을 중복 사용하지 않음
#     for cap in range(k, w - 1, -1):
#         dp[cap] = max(dp[cap], dp[cap - w] + v)

# print(dp[k])