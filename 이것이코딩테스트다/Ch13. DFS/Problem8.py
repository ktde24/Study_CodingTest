# 블록 이동하기(https://school.programmers.co.kr/learn/courses/30/lessons/60063)
from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 이동 가능한 위치들
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우 이동하는 경우 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]

        # 이동하고자 하는 두 칸이 모두 비어 있으면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있으면
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽이나 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:  # 위쪽이나 아래쪽 두 칸이 모두 비어있으면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 세로로 놓여 있으면
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 위쪽이나 아래쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:  # 위쪽이나 아래쪽 두 칸이 모두 비어있으면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos  # 현재 위치에서 이동할 수 있는 위치


def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # BFS
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작 위치
    q.append((pos, 0))  # 큐에 삽입
    visited.append(pos)  # 방문 처리
    # 큐가 빌 때까지
    while q:
        pos, cost = q.popleft()
        # (n,n) 위치에 도달했으면, 최단거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0