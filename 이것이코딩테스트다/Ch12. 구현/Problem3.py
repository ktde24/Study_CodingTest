# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057?gad_source=1&gad_campaignid=22199869887&gbraid=0AAAAAC_c4nCBRuVKK6Fk376z9O5jWUFGB&gclid=Cj0KCQjwm93DBhD_ARIsADR_DjFMh6QfxQS9bUAhEw5JoS-M0Qf7wOT8ilarkyOAZsrIXriFX01Bp_caAlHAEALw_wcB

# 입력으로 주어지는 문자열의 길이가 1000이하 => 가능한 모든 경우의 수 탐색하는 완전 탐색 수행

def solution(s):
    answer = []

    if len(s) == 1:  # 문자열 s의 길이가 1인 경우, 압축할 필요X
        return 1

    for i in range(1, len(s)//2 + 1): # s를 길이가 i인 부분 문자열 단위로 나누기
        result = '' # 현재 압축된 문자열을 저장
        tmp = s[:i] # 현재 비교 중인 부분 문자열
        cnt = 1 #  현재 tmp와 동일한 부분 문자열의 반복 횟수
        for j in range(i, len(s), i):  # 압축 단위 i만큼 건너뛰며 문자열의 각 부분을 순회
            if tmp == s[j:j+i]: # 현재 tmp와 다음 부분 문자열 s[j:j+i]가 같으면 cnt를 증가
                cnt += 1
            else: # 현재 tmp와 다른 부분 문자열이 나타난 경우
                if cnt > 1: # cnt가 2 이상이면 반복된 횟수와 함께 tmp를 result에 추가
                    result += str(cnt) + tmp
                else: # 반복이 없으면 그대로 tmp를 result에 추가
                    result += tmp
                cnt = 1 # 반복 횟수를 초기화하고 tmp를 현재 부분 문자열로 갱신
                tmp = s[j:j+i]
        if cnt > 1:  #반복된 부분 문자열은 반복 횟수와 함께 추가
            result += str(cnt) + tmp
        else: # 반복이 없는 경우 그대로 추가
            result += tmp
        answer.append(len(result))
    return min(answer)