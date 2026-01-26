import sys
from math import inf

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
graph = []
for _ in range(m):
    s, e, c = [int(x) for x in input().split()]
    graph.append((s, e, c))

res = [inf] * (n + 1)
res[1] = 0

for i in range(n - 1):
    for g in graph:
        s, e, c = g
        if (nr := (res[s] + c)) < res[e]:
            res[e] = nr

for g in graph:
    s, e, c = g
    if (nr := (res[s] + c)) < res[e]:
        res = [0, 0, -1]
        break

for r in res[2:]:
    if r == inf:
        print(-1)
    else:
        print(r)

## 정석 벨만포드
# import sys
# from math import inf

# input = sys.stdin.readline

# # map을 쓰면 리스트 컴프리헨션보다 미세하게 빠르고 코드가 깔끔해집니다.
# n, m = map(int, input().split())
# graph = []
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     graph.append((s, e, c))

# res = [inf] * (n + 1)
# res[1] = 0

# # 3. 음수 사이클 존재 여부 확인 플래그
# cycle = False

# # N번 반복 (N-1번은 최단거리 갱신, 마지막 1번은 사이클 확인용)
# for i in range(n):
#     # 2. 이번 라운드에서 갱신이 일어났는지 체크 (Early Exit)
#     updated = False 
    
#     for s, e, c in graph:
#         # 1. 방문한 적 있는 노드(출발지에서 도달 가능)인 경우에만 갱신 시도
#         if res[s] != inf and res[s] + c < res[e]:
#             res[e] = res[s] + c
#             updated = True
            
#             # N번째 라운드(i == n-1)에서도 갱신이 일어난다면 음수 사이클 존재
#             if i == n - 1:
#                 cycle = True
    
#     # 2. 더 이상 갱신이 안 되면, 남은 반복을 돌 필요가 없음 (시간 단축 핵심)
#     if not updated:
#         break

# if cycle:
#     print(-1)
# else:
#     # 2번 노드부터 출력
#     for r in res[2:]:
#         # 도달할 수 없는 경우 -1 출력 (문제 조건)
#         print(r if r != inf else -1)