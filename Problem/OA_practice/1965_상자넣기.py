n = int(input())
boxes = [int(x) for x in input().split()]
cnts = [1 for _ in range(n)]
for i in range(1, n):
    tmp = 0 
    for j in range(i, -1, -1):
        if boxes[j] < boxes[i] and tmp < cnts[j]:
            tmp = cnts[j]
    cnts[i] += tmp

print(max(cnts))