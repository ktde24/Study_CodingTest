# 미래도시
# 판매원 A는 현재 1번 회사에 위치, X번 회사에 방문하여 물건을 판매하고자 함
# 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일
# A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사(Kqjs)에 찾아갈 예정
# A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램 작성

INF = int(1e9) # 무한: 10억

# 입력 받기
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 만들기

# 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 X와 최종 목적지 노드 K 입력받기
x, k= map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

dist = graph[1][k] + graph[k][x]

if dist >= INF: # 도달할 수 없는 경우
    print("-1")
else:
    print(dist)