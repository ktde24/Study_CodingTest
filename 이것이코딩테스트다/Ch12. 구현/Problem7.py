# 치킨 배달(https://www.acmicpc.net/problem/15686)

# 기존에 존재하는 치킨집을 줄여서 최대 M개로 유지하면서, M개의 치킨집까지의 거리를 줄이기

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))
# 모든 치킨집 중 m개의 치킨집 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리 합 계산
def get_sum(candidate):
    res = 0
    # 모든 집에 대해
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        res += temp # 가장 가까운 치킨집까지의 거리 더하기
    return res # 치킨 거리 합 반환

res = 1e9
for candidate in candidates:
    res = min(res, get_sum(candidate))
print(res)