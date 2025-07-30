# 인구 이동
# https://www.acmicpc.net/problem/16234

from collections import deque

# 입력: N(격자 크기), L(최소 인구 차이), R(최대 인구 차이)
n, l, r = map(int, input().split())

# 각 나라(격자 칸)의 인구 수 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 인접한 네 방향: 북, 서, 남, 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 연합을 구성하고 인구를 이동시키는 함수
def process(x, y, index):
    # 현재 위치를 시작으로 연합에 포함
    united = [(x, y)]

    # BFS를 위한 큐 생성
    q = deque()
    q.append((x, y))

    # 현재 위치의 연합 번호 할당
    union[x][y] = index

    # 현재 연합의 인구 총합과 국가 수 초기화
    summary = graph[x][y]
    count = 1

    # BFS 실행
    while q:
        x, y = q.popleft()

        # 상하좌우 인접 국가 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 아직 처리되지 않은 국가라면
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 인구 차이가 L 이상 R 이하인 경우, 연합 가능
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index  # 연합 번호 할당
                    summary += graph[nx][ny]  # 인구 합산
                    count += 1  # 국가 수 증가
                    united.append((nx, ny))  # 연합 국가 리스트에 추가

    # 연합 내 인구를 평균 인구로 갱신
    for i, j in united:
        graph[i][j] = summary // count

    # 이번에 생성된 연합의 국가 수 반환
    return count


# 인구 이동이 발생한 총 횟수
total_count = 0

# 인구 이동이 더 이상 일어나지 않을 때까지 반복
while True:
    # 연합 정보를 담을 배열: -1은 아직 처리되지 않음을 의미
    union = [[-1] * n for _ in range(n)]
    index = 0  # 연합 번호 (0부터 시작)

    # 모든 칸을 탐색하여 연합을 구성
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                # 현재 위치에서 BFS로 연합 구성
                process(i, j, index)
                index += 1

    # 연합 수가 전체 칸 수와 같으면 → 모든 칸이 독립적 → 이동 종료
    if index == n * n:
        break  # 더 이상 인구 이동 없음

    # 이동이 일어났으므로 하루 증가
    total_count += 1

# 결과 출력: 총 인구 이동 일수
print(total_count)
