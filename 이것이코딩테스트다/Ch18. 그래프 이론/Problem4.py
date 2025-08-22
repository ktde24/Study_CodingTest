# 행성 터널
# 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램 작성

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

n = int(input())
parent = [0] * (n+1)
edges = []
result = 0

# 부모를 자기 자신으로
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보 추출하여 처리
for i in range(n-1):
    # 비용순 정렬
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순 정렬
edges.sort()

# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)