P, M = map(int, input().split())
rooms =[]
for i in range(P):
    level, name = input().split()
    level = int(level)
    is_in = False
    for room in rooms:
        if room[0] - 10 <= level <= room[0] + 10 and len(room[1]) < M:
            room[1].append((level, name))
            is_in = True
            break
    if not is_in:
        rooms.append([level,[(level, name)]])

for room in rooms:
    if len(room[1]) == M:
        print("Started!")
    else:
        print("Waiting!")
    
    room[1].sort(key= lambda x: x[1])
    for l,n in room[1]:
        print(l, n)