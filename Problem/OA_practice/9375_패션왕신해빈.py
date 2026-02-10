num_case = int(input())
list_res = []
for i in range(num_case):
    n = int(input())
    if n:
        list_n = [[x,y] for x, y in (input().split() for _ in range (n))]
        dict_n = {}
        for x,y in list_n:
            if y in dict_n:
                dict_n[y].append(x)
            else:
                dict_n[y] = [x]
        
        res = 1
        for l in dict_n.values():
            res *= (len(l) + 1)
        list_res.append(res - 1)
    else:
        list_res.append(0)

for res in list_res:
    print(res)