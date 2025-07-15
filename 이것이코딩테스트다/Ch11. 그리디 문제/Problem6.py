# 무지의 먹방 라이브(https://school.programmers.co.kr/learn/courses/30/lessons/42891?gad_source=1&gad_campaignid=22199869887&gbraid=0AAAAAC_c4nCaJac--MCFFHxtN3qLU9mn0&gclid=CjwKCAjw1dLDBhBoEiwAQNRiQYCZ7kn8MExEVTsgzHrI2_yK6KOsTlGyu3emlLgQcofcx5jdXgVOwRoCh0UQAvD_BwE)

import heapq
def solution(food_times, k):
    if sum(food_times) <= k: # 전체 음식을 먹는 시간보다 k가 크거나 같으면
        return -1

   # 시간이 작은 음식부터 빼기 => 우선순위 큐
   q = []
   for i in range(len(food_times)):
       # (음식 시간, 음식 번호) 형태로 우선순위 큐 삽입
        heapq.heappush(q, (foot_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 다시 설정

    # 남은 음식 중 몇 번째 음식인지 확인하여 출력
    res = sorted(q, key=lambda x:[1]) # 음식 번호 기준 정렬
    return result[(k-sum_value) % length][1]