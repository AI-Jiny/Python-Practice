import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[[inf, []]for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i][0] = 0
    graph[i][i][1].append(i)

for _ in range(m):
    s, e, c = map(int, input().split())
    if c < graph[s][e][0]:
        graph[s][e][0] = c
        graph[s][e][1] = [s, e]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (nc := (graph[i][k][0] + graph[k][j][0])) < graph[i][j][0]:
                graph[i][j][0] = nc
                graph[i][j][1] = graph[i][k][1] + graph[k][j][1][1:]

for g in graph[1:]:
    ans = []
    for n in g[1:]:
        if n[0] != inf:
            ans.append(n[0])
        else:
            ans.append(0)
    
    print(" ".join(map(str, ans)))

for g in graph[1:]:
    for n in g[1:]:
        if n[0] != inf and len(n[1]) > 1:
            print(len(n[1]), end=" ")
            print(" ".join(map(str, n[1])))
        else:
            print(0)


# ### 정석
# import sys
# # 
# # 경로 배열(nxt)을 따로 만들어 "i에서 j로 갈 때 가장 먼저 거쳐야 하는 노드"를 저장합니다.

# input = sys.stdin.readline
# INF = sys.maxsize

# n = int(input())
# m = int(input())

# # 1. 비용 배열과 경로 배열(Next Node) 초기화
# # cost[i][j]: i -> j 최소 비용
# # nxt[i][j]: i -> j 로 최단거리로 갈 때, i 다음에 바로 가야할 노드
# cost = [[INF] * (n + 1) for _ in range(n + 1)]
# nxt = [[0] * (n + 1) for _ in range(n + 1)]

# # 자기 자신으로 가는 비용은 0
# for i in range(1, n + 1):
#     cost[i][i] = 0

# # 2. 간선 입력 받기
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     if c < cost[s][e]:
#         cost[s][e] = c
#         nxt[s][e] = e  # s에서 e로 가는 최단 경로는 바로 e로 가는 것 (초기 상태)

# # 3. 플로이드-워셜 알고리즘
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             # i -> k -> j 가 i -> j 보다 빠르다면 갱신
#             if cost[i][k] + cost[k][j] < cost[i][j]:
#                 cost[i][j] = cost[i][k] + cost[k][j]
#                 # 중요: i에서 j로 가는 길을 k를 거쳐서 가기로 했으므로,
#                 # i 다음 방문할 곳은 'i에서 k로 갈 때의 다음 노드'와 같음
#                 nxt[i][j] = nxt[i][k]

# # 4. 비용 출력
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if cost[i][j] == INF:
#             print(0, end=" ")
#         else:
#             print(cost[i][j], end=" ")
#     print()

# # 5. 경로 복원 및 출력
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         # 갈 수 없거나 자기 자신인 경우
#         if cost[i][j] == INF or i == j:
#             print(0)
#             continue
        
#         # 경로 추적 시작
#         path = []
#         curr = i
#         while curr != j:
#             path.append(curr)
#             curr = nxt[curr][j] # curr에서 j로 가려면 다음에 어디로 가야하지?
#         path.append(j) # 마지막 도착지 추가
        
#         print(len(path), end=" ")
#         print(*path)