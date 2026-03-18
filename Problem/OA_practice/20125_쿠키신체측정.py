N = int(input())
maps = []
heart = None


for i in range(N):
    maps.append(input())

for i in range(N):
    for j in range(N):
        if maps[i][j] == "*":
            heart = (i + 1, j)
    if heart:
        break

for i in range(N):
    m = maps[heart[0]][i]
    if m == "*":
        left = heart[1] - i
        break

for i in range(N - 1, heart[1], -1):
    m = maps[heart[0]][i]
    if m == "*":
        right = i - heart[1]
        break

for i in range(heart[0] + 1, N):
    n = maps[i][heart[1]]
    if n == "_":
        waist = i - heart[0] - 1
        ls = (i, heart[1])
        break
legs = []
for r in [-1, 1]:
    la, lb = ls
    lb += r
    leg = 0
    for i in range(la, N):
        if maps[i][lb] == "*":
            leg += 1
        else:
            break        
    legs.append(leg)

print(heart[0] + 1, heart[1] + 1)
print(left, right, waist, legs[0], legs[1])