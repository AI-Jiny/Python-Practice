N = int(input())
list_n = sorted([int(x) for x in input().split()])
X =  int(input())
set_n = set(list_n)
ans = 0

for n in list_n:
    if X - n in set_n:
        ans += 1

print(ans // 2)