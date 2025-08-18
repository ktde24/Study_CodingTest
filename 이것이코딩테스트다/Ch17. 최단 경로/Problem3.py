# 화성 탐사
# 첫째 줄에 테스트 케이스 수 T가 주어짐
# 매 테스트케이스틔 첫째 줄에는 탐사공간의 크기를 의미하는 정수 N이 주어짐. 이어 N개의 줄에 걸쳐 각 칸의 비용이 주어짐
# 가장 왼쪽 위칸에서 가장 오른쪽 아래 칸으로 이동하는 최소 비용 출력하는 프로그램 작성

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 TC만큼
for tc in range(int(input())):
    n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 최단 거리 테이블 무한으로 초기화
distance = [[INF] * n for _ in range(n)]

x, y = 0, 0 # 시작 위치
# 시작 노드로 가기 위한 비용은 (0, 0)위치의 값으로 설정하여 큐에 삽입
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

while q:
    # 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, x, y = heapq.heappop(q)
    # 현재 노드가 이미 처리된적이 있는 노드면 무시
    if distance[x][y] < dist:
        continue
    # 현재 노드와 연결된 다른 인접 노드들 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 맵의 범위를 벗어나는 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        cost = dist + graph[nx][ny]
        # 현재 노드 거쳐서, 다른 노드로 이동하는 경우가 더 짧은 경우
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))
print(distance[n-1][n-1])