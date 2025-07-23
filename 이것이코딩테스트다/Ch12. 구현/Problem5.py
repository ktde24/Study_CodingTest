# 뱀
# N * N 정사각 보드. 몇몇 칸에는 사과 존재. 보드의 상하좌우 끝에는 벽. 뱀의 길이는 1
# 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킴
# 만약 이동한 칸에 사과가 있으면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 X
# 이동한 칸에 사과가 없으면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌. 즉, 몸길이는 변하지 X
# 사과의 위치, 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하기

n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전

# 맵(사과: 1)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 정보
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에 오른쪽 보고 있음
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀 머리
    data[x][y] = 2 # 뱀이 존재하는 위치는 2
    direction = 0
    time = 0 # 시작 후 지난 초 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 잆고, 뱀의 몸통이 X
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과 없으면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1: # 사과가 있으면 꼬리 그대로
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀 몸통과 부딪히면
        else:
            time += 1
            break
        x, y = nx, ny  #다음 위치로 머리 이동
        time += 1
        if index < 1 and time == info[index][0]: # 회전할 시간이면 회전
            direction = turn(direction, info[index][1])
            index += 1
        return time
    print(simulate())