# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# 모든 간선의 비용일 동일할 때: BFS(너비 우선 탐색) 이용하여 최단거리 찾기 가능

from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 도로 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면 거리 = 현재 도시 거리 + 1 & 큐에 추가해서 이후 탐색
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
# 최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 최단거리가 K인 도시가 없으면
if check == True:
    print(-1)