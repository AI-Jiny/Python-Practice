N = int(input())
list_n = [int(x) for x in (input() for _ in range(N))]
dict_v = {0:1, 1:1, 2:2}

def get_v(n):
    if n in dict_v:
        return dict_v[n]
    
    value = get_v(n - 3) + get_v(n - 2) + get_v(n - 1)
    dict_v[n] = value
    return value

for n in list_n:
    print(get_v(n))
