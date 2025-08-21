# 여행 계획
# 1~N번까지의 여행지. 여행지가 도로로 연결되어 있다면 양방향으로 이동 가능
# 여행 계획을 세운 뒤, 이 여행계획이 가능한지의 여부를 판단하려고 함
# 여행지 개수, 여행지 간 연결정보가 주어졌을 때, 여행계획이 가능한지 여부를 판단하는 프로그램 작성


# 여행 계획에 해당하는 모든 노드가 같으 집합에 속하면 여행 가능

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

n, m = map(int, input().split()) # n: 여행지수, m: 여행계획에 속한 도시 수
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union 연산
            union_parent(parent, i+1, j+1)

# 여행 계획 입력
plan = list(map(int, input().split()))
result = True

# 여행 계획에 속하는 모든 노드의 루트가 동일한지
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인
if result:
    print("YES")
else:
    print("NO")