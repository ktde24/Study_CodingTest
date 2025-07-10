# 팀 결성
# 학생들에게 0번부터 N번까지 번호 부여. 처음에는 총 N+1개의 팀이 존재.
# 팀 합치기 연산: 두 팀을 합치는 연산
# 같은 팀 여부 확인: 연산은 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산
# 선생님이 M개의 연산을 수행할 수 있을 때, 같은 팀 여부 확인 연산에 대한 연산 결과 출력하는 프로그램 작성
# 팀 합치기 연산은 0 a b 형태로 주어짐 => a번 학생이 속한 팀과 b번 학생이 속한 팀을 합치기
# 같은 팀 여부 확인 연산 => 1 a b 형태로 주어짐. a번 학생과 b번 학생이 같은 팀에 속해있는지 확인

# 특정 원소가 속한 집합 찾기
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

n, m = map(int, input().split())
parent = [0] * (n+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합인 경우
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')