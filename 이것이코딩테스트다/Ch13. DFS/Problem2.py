# 연구소
# https://www.acmicpc.net/problem/14502

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 후의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0

# DFS 이용하여 각 바이러스가 사방으로 퍼지도록
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중 바이러스가 더 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS 이용해 울타리 설치하면서, 매번 안전 영역 크기 계산
def dfs(count):
    global res
    # 울타리가 3개 설치된 경우(1. 임시 맵에 원본 복사)
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스 위치에서 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        res = max(res, get_score())
        return
    # 빈 공간에 울타리 설치(이중 반복문으로 빈칸을 찾아 벽을 하나 세우고, 재귀 호출로 나머지 벽 2개를 설치 & 설치 완료 후 → 바이러스 퍼뜨리고 안전 영역 계산 & 백트래킹으로 이전 상태로 되돌림)
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(res)