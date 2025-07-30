# 감시 피하기
# https://www.acmicpc.net/problem/18428

from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 선생님 위치 정보
spaces = [] # 빈 공간 위치

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
        # 장애물 설치할 수 있는 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))

# 특정 방향으로 감시 진행(학생 발견: True, 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    # 오른쪽 방향
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    # 위쪽 방향
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽 방향
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return  False

# 장애물 설치 후, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치 확인
    for x, y in teachers:
        # 4가지 방향으로 학생 감지 가능한지
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않으면
    if not process():
         # 원하는 경우 발견한 것
        find = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')