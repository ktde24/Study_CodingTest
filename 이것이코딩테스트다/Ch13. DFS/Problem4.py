# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058?gad_source=1&gad_campaignid=22799790467&gbraid=0AAAAAC_c4nCXdzN0qERWof0582maRt_dm&gclid=CjwKCAjwv5zEBhBwEiwAOg2YKDLqpkho0y93984zwiHffSftYcytOI0G5paNh4kMk-D6LVmZB-u97RoCE04QAvD_BwE
# 균형 잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    cnt = 0  # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


# 올바른 괄호 문자열인지 판단
def check_proper(p):
    cnt = 0  # 왼쪽 괄호 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:  # 쌍이 맞지 않는 경우
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면, v에 대해 함수 수행한 결과를 붙여서 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫번째 문자, 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer