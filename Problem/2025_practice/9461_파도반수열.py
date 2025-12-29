n = int(input())
list_q = [int(x) for x in (input() for _ in range(n))]
memo = {1: 1, 2: 1, 3: 1}

def get_v(n):
    if n in memo:
        return memo[n]

    val = get_v(n -3) + get_v(n - 2)
    memo[n] = val
    return val

for q in list_q:
    print(get_v(q))