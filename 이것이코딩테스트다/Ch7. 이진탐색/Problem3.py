# 떡볶이 떡 만들기
# 떡볶이 떡의 길이가 일정하지 X. 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다. 절단기에 높이(H)를 지정하면, 한 번에 절단
# 높이가 H보다 긴 떡은 H 위의 부분이 잘림.
# 예를 들어, 19, 14, 10, 17cm 떡이 있고 절단기 높이를 15cm로 하면 => 잘린 떡의 길이: 4, 0, 0, 2cm => 6cm 길이를 가져감
# 손님이 왔을 때 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기

n, m = list(map(int, input().split()))
arr = list(map(int, input().split())) # 각 떡의 개별 높이 정보

start = 0
end = max(arr)

res = 0

while(start <= end):
    total = 0

    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid

    if total < m: # 떡의 양이 부족하면
        end = mid - 1
    else: # 떡의 양이 충분하면 덜 자르기
        res = mid
        start = mid + 1
print(res)