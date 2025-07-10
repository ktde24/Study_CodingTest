# 도시 분할 계획
# 마을은 N개의 집과 M개의 길로 이루어져 있다.
# 마을을 분할할 때, 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻
# 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있음
# 길의 유지비의 합을 최소화하기 위한 프로그램 작성
# 츨력:길을 없애고 남은 유지비 합의 최솟값

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트 & 최종 비용 담을 변수
edges = []
res = 0

# 부모 테이블 상에서 부모 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순 정렬 위해, 튜플의 첫 원소를 비용으로 설정
    edges.append((cost, a, b))

# 비용순 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        last = cost

print(res-last)