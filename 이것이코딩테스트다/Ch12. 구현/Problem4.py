# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059
# 열쇠를 나타내는 2차원 배열 key, 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 true, 없으면 false를 return

# 자물쇠를 큰 보드 중앙에 배치
# 열쇠를 4번(0도, 90도, 180도, 270도) 회전하면서:
# 열쇠를 보드의 가능한 모든 위치에 올려보기 & 올려놓고 자물쇠가 열렸는지 검사 & 열쇠를 다시 제거하고 다음 위치로 진행

def attach(x, y, M, key, board): # 열쇠 값이 1이면, 보드 값도 1 증가 (덮는 효과)
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board): # 값을 빼서 원상복구
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]


def rotate90(arr): # 열쇠를 90도 시계 방향으로 회전
    return list(zip(*arr[::-1]))


def check(board, M, N): # 드에서 자물쇠 영역(M~M+N)을 확인
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False;
    return True # 해당 영역이 모두 1이면 자물쇠가 열림


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if (check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)

    return False
