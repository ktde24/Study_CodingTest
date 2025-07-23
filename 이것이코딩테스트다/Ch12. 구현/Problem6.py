# 기둥과 보 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/60061?gad_source=1&gad_campaignid=22799790467&gbraid=0AAAAAC_c4nAGpct24IX9uOz5q233KZoPK&gclid=CjwKCAjw7fzDBhA7EiwAOqJkh2ciGjzBORUrliwoHoRO1j_MNVskmGFCbsGG2tLIXV2Jv5KIG6ClGxoCJvkQAvD_BwE

# 현재 구조물이 정상인지 체크하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥이면
            # 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있으면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False # 아니면 거짓 반환
        elif stuff == 1: # 보이면
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있으면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff]) # 일단 삭제
            if not possible(answer):
                answer.append([x, y, stuff]) # 가능한 구조물이 아니면 다시 설치
        if operate == 1:
            answer.append([x, y, stuff]) # 일단 설치
            if not possible(answer):
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니면 다시 삭제
    return sorted(answer)