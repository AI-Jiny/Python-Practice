r, c = map(int, input().split())
visited = {}
ans = 0

def roll(top, front, right, direction):
    ntop, nfront, nright = top, front, right
    if direction == "right":
        ntop = 7 - right
        nright = top
    elif direction == "left":
        ntop = right
        nright = 7 - top
    elif direction == "down":
        ntop = 7 - front
        nfront = top
    
    return ntop, nfront, nright


ans += (c // 4) * r * 14
nc = c % 4
dice = (1,2,3)
for i in range(r):
    if nc:
        for j in range(nc - 1):
            direction = "left" if (i % 2) else "right"
            t, f, r = dice
            dice = roll(t, f, r, direction)
            ans += t

        t, f, r = dice
        ans += t
        dice = roll(t, f, r, "down")

print(ans)

        


    
