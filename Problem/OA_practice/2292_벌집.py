target = int(input())
r = 1

if target == 1:
    print(1)
else:
    while not (s:= (r * (r - 1) * 3 + 2)) <= target <= (e:= (r * (r + 1) * 3 + 1)):
        r += 1
    print(r + 1)


## 정석
# target = int(input())

# cur = 1
# ring = 1

# while target > cur:
#     cur += ring * 6
#     ring += 1

# print(ring)