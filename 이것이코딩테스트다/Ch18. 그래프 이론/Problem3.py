# 어두운 길
# 한 마을은 N개의 집과 M개의 도로로 구성되어 있다. 집은 0번부터 N-1번까지의 번호로 구분됨
# 특정 도로의 가로등을 하루동안 켜기 위한 비용 = 해당 도로의 길이
# 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액 출력하기

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면, 찾을 때까지 재귀 호출
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

n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블

# 간선 담을 리스트, 최종 비용 담을 변수
edges = []
result = 0

# 부모를 자기 자신으로
for i in range(1, n+1):
    parent[i] = i

# m개의 줄에 걸쳐, 도로에 대한 정보 X, Y, Z 주어짐(X번 집과 Y번 집 사이에 양방향 도로가 있고, 그 길이가 Z)
 for _ in range(m):
     x, y, z = map(int, input().split())
     # 비용순 정렬 위해 튜플의 첫 번째 원소를 비용으로
     edges.append((z, x, y))

# 간선을 비용순 정렬
edges.sort()
total = 0

# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    total += cost
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(total - result)
