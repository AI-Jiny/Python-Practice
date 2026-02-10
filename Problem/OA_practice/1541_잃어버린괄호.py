list_s = input().split("-")
res = sum(int(x) for x in list_s[0].split("+"))
for s in list_s[1:]:
    res -= sum(int(x) for x in s.split("+"))

print(res)



