# 공유기 설치(https://www.acmicpc.net/problem/2110)

# 가장 인접한 두 공유기 사이의 거리 최댓값 탐색하는 문제
n, c = list(map(int, input().split()))

# 전체 집 좌표 정보
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행 위한 정렬

start = 1 # 가능한 최소 거리
end = array[-1] - array[0] # 가능한 최대 거리
res = 0

while(start <= end):
    mid = (start+end) // 2 # 가장 인접한 두 공유기 사이의 거리
    value = array[0]
    count = 1
    # 현재의 mid값 이용해 공유기 설치
    for i in range(1,n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기 설치할 수 있으면 거리 증가
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)