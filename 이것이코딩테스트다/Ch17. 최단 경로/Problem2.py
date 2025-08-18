# 정확한 순위
# 시험을 본 학생 N명의 성적 분실. 성적을 비교한 결과의 일부만 가지고 있음
# 첫째줄에 학생들의 수 N, 두 학생의 성적을 비교한 횟수 M이 주어짐
# 다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A, B가 주어짐 => A번 학생의 성적이 B번 학생보다 낮다는 것을 의미
# 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램 작성

# A에서 B로 도달 가능 or B에서 A로 도달 가능 = 성적 비교 가능한 것
INF = int(1e9)

n, m = map(int, input().split())
# 2차원 리스트 만들고, 모든 값을 무한으로
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)