n,m = [int(x) for x in input().split()]
set_n = {input() for _ in range(n)}
set_m = {input() for _ in range(m)}

list_nm = sorted(list(set_n & set_m))
print(len(list_nm))
for nm in list_nm:
    print(nm)
