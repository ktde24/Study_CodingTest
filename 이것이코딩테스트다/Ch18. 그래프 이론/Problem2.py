# 탑승구
# 공항에는 1~G번까지의 탑승구 존재
# P개의 비행기가 차례로 도착. i번째 비행기를 1번부터 g_i번쨰 탑승구 중 하나에 도킹해야 함
# P개의 비행기를 순서대로 도킹하다가 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오면, 공항 운행 중지
# 비행기를 최대 몇 대 도킹할 수 있는지 출력
# 첫째줄: 탑승구 수(G), 둘쨰줄: 비행기 수(P), 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구 정보(gi: i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹 가능)

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

# 입력
g = int(input())
p = int(input())
parent = [0] * (g+1) # 부모 테이블 초기화

# 부모를 자기 자신으로
for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 루트가 0이면, 더 이상 도킹이 불가능한 것으로 판단
        break
    union_parent(parent, data, data-1)
    result += 1
print(result)