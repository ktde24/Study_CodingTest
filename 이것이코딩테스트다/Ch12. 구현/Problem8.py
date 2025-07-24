# 외벽 점검
# https://school.programmers.co.kr/learn/courses/30/lessons/60062?gad_source=1&gad_campaignid=22799790467&gbraid=0AAAAAC_c4nANwApULyBkXXG0nawbbI602&gclid=Cj0KCQjws4fEBhD-ARIsACC3d28g1dqakZRWTcxGrsLYuSdOR8Bzuydlw0RsDOs4HP-IisXLP8HmGBUaAqLpEALw_wcB
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값 찾아야 하므로 초기화
    # 0부터 lenght - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dist, len(dist))):
            cnt = 1 # 투입할 친구수
            # 해당 친구가 점검할 수 있는 마지막 위치
            pos = weak[start] + friends[cnt - 1]
            # 시작점부터 모든 취약 지점 확인
            for idx in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if pos < weak[idx]:
                    cnt += 1 # 새로운 친구 투이
                    if cnt > len(dist): # 더 이상 투입 불가능하면 종료
                        break
                    pos = weak[idx] + friends[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer