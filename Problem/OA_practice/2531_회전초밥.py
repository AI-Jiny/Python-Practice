from collections import Counter

N, D, K, C = map(int,input().split())
objs = []
for _ in range(N):
    objs.append(int(input()))

objs *= 2
window = Counter(objs[:K])
window[C] = 1
ans = len(window.keys())
cur_cnt = ans

if ans == K + 1:
    print(ans)
else:
    for idx in range(N):
        pre_obj = objs[idx]
        nxt_obj = objs[idx + K]
        if pre_obj != C:
            window[pre_obj] -= 1
            if not window[pre_obj]:
                del window[pre_obj]
                cur_cnt -= 1
        if nxt_obj != C:
            nxt_obj_cnt = window.get(nxt_obj, 0)
            if not nxt_obj_cnt:
                cur_cnt += 1
            window[nxt_obj] = nxt_obj_cnt + 1
        if ans < cur_cnt:
            ans = cur_cnt
        if ans == K + 1:
            break
        print(window)
    print(ans)        
    

# 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d
# 8 30 4 30
# 7
# 9
# 7
# 30
# 2
# 7
# 9
# 25