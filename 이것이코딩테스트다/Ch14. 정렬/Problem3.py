# 실패율(https://school.programmers.co.kr/learn/courses/30/lessons/42889)
def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N + 1):

        # 해당 스테이지에 머물러 있는 사람
        cnt = stages.count(i) #  # i번 스테이지에 "멈춰 있는 유저 수" 세기

        # 실패율
        if length == 0: # 도달한 유저가 없으면 실패율은 0
            fail = 0
        else:
            fail = cnt / length # 실패율 = 클리어 못 한 사람 / 도달한 사람

        # 리스트에 (스테이지 번호, 실패울) 삽입
        answer.append((i, fail))
        length -= cnt # 다음 스테이지의 분모에서 제외 (다음 스테이지 도달자 수 갱신)
    # 실패율 기준 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer







