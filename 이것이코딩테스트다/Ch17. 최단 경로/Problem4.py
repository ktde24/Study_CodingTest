# 숨바꼭질
# 1~N번까지의 헛간 중 하나를 골라 숨을 수 이으며, 술래는 항상 1번 헛간에서 출발
# 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결.
# 1번 헛간으로부터 최단 거리가 가장 먼 헛간의 번호 찾기(거리가 같은 헛간이 여러개면 가장 작은 번호 출력)
# 숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를ㄹ 갖는 헛간 개수 출력


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# 시작노드를 1번 헛간으로
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드와 b번 노드의 이동 비용이 1
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단거리와 동일한 최단 거리 가지는 노드들
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))