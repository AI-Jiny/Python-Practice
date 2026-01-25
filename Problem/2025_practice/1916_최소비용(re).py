import heapq
from math import inf

N = int(input())
M = int(input())
list_m = [[int(x) for x in input().split()] for _ in range(M)]
start, end = [int(x) for x in input().split()]
dict_m = {}
list_ans = [inf] * (N + 1)
list_ans[start] = 0
not_visited = {int(x) for x in range(1, N + 1)}
cur = [start]


for s, e, c in list_m:
    dict_m.setdefault(s, {})
    dict_m[s][e] = min(dict_m[s].get(e, inf), c)
        
while cur:
    s = cur.pop()
    if s not in not_visited:
        continue
    if s in dict_m:
        for e, c in dict_m[s].items():
            if (cc := (list_ans[s] + c)) < list_ans[e]:
                list_ans[e] = cc

    
    not_visited.remove(s)
    
    heap = []
    for nt in not_visited:
        heapq.heappush(heap, (list_ans[nt], nt))
    
    if heap:
        nxt = heapq.heappop(heap)[1]
        cur.append(nxt)

print(list_ans[end])


## 정석 코드
# import heapq
# import sys
# input = sys.stdin.readline
# from math import inf

# N = int(input())
# M = int(input())
# # 인접 리스트 생성
# graph = [[] for _ in range(N + 1)]
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))

# start, end = map(int, input().split())

# # 다익스트라 초기화
# dist = [inf] * (N + 1)
# dist[start] = 0
# queue = []
# heapq.heappush(queue, (0, start)) # (비용, 노드)

# while queue:
#     current_dist, current_node = heapq.heappop(queue)

#     # 이미 처리된 적 있는 노드라면(더 짧은 경로가 이미 발견됨) 스킵
#     if dist[current_node] < current_dist:
#         continue
    
#     for next_node, weight in graph[current_node]:
#         next_dist = current_dist + weight
#         if next_dist < dist[next_node]:
#             dist[next_node] = next_dist
#             heapq.heappush(queue, (next_dist, next_node))

# print(dist[end])