# 카드 정렬하기(https://www.acmicpc.net/problem/1715)
# 우선순위 큐: 원소를 넣었다 빼는 것만으로도 정렬된 결과 얻을 수 있음

import heapq

n = int(input())

# heap에 초기 카드 묶음 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data) # 카드 묶음을 최소 힙에 추가

res = 0

# heap에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)  # 가장 작은 카드 묶음
    two = heapq.heappop(heap)
    # 카드 묶음 합쳐서 다시 삽입
    sum_value = one + two
    res += sum_value
    heapq.heappush(heap, sum_value)
print(res)