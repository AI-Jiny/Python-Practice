n = int(input())
n_list = [[int(x),y] for x,y in (input().split() for _ in range(n))]
n_list.sort(key=lambda x: x[0])

for age, name in n_list:
    print(f"{age} {name}")