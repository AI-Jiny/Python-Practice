t = int(input())
ans = []
for idx in range(1, t + 1):
    children = [int(x) for x in input().split()][1:]
    cnt = 0
    for i, child in enumerate(children):
        for j in range(i):
            if children[j] > child:
                cnt += 1
    ans.append([idx, cnt])

for an in ans:
    print(an[0], an[1])
