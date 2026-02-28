from collections import deque

S = input()
T = input()
flg = False

dq = deque([])
dq.append(S)

while dq:
    s = dq.popleft()
    if s == T:
        print(1)
        flg = True
        break

    t1 = f"{s}A"
    t2 = f"{s}B"[::-1]

    nxt = set()
    nxt.add(t1)
    nxt.add(t2)

    for w in list(nxt):
        if w in T or w[::-1] in T:
            dq.append(w)
    
if not flg:
    print(0)    