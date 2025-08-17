# 플로이드(https://www.acmicpc.net/problem/11404)

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
INF = int(1e9) # 무한

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 만들고, 모든 값 무한으로 초기화

# 자기자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없으면 0
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()