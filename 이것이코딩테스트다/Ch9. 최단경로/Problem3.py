# 전보
# N개의 도시. 전보를 보내려면 통로가 있어야 함. X에서 Y로 향하는 통로는 있지만 Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 X
# C라는 도시에 위급 상황 발생. 최대한 많은 도시로 메시지를 보내고자 함
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수, 메시지를 받는 데까지 걸리는 시간 계산하는 프로그램

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대ㅏㄴ 정보 담는 리스트
distance = [INF] * (n+1) # 최단 거리 테이블을 무한으로 초기화

# 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z)) # x번 노드에서 y번 노드로 가는 비용이 z


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

count = 0 # 도달할 수 있는 노드 개수
# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_dist = 0
for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

print(count-1, max_dist) # 시작 노드는 제외