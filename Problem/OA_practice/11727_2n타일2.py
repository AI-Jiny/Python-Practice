n = int(input())
memo = {1: 1, 2: 3}

def get_v(n):
    if n in memo:
        return memo[n]
    
    val = get_v(n - 2) * 2 + get_v(n - 1)
    memo[n] = val
    return val

print(get_v(n) % 10007)

"""
1 : 1
2 : 3
3 : 2 + 3 = 5
"""