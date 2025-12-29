n = int(input())
memo = {1: 1, 2: 2}

def get_v(n):
    if n in memo:
        return memo[n]
    
    val = get_v(n - 1) + get_v(n - 2)
    memo[n] = val
    return val

print(get_v(n) % 10007)