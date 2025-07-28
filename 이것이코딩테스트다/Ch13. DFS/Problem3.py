# 경쟁적 전염(https://www.acmicpc.net/problem/18405)

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(n):
    # 보드 정보 한 줄 단위로 입력 받기
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽임
            data.append((graph[i][j], 0, i, j))

# 정렬 후 큐로 옮기기(낮은 번호 바이러스가 먼저 증식하니까)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼질 수 있는 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나 큐가 빌 때까지
    if s == target_s:
        break
    for i in range(4): # 현재 노드에서 주변 4가지 위치 확인
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동 가능한 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치면 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])