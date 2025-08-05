# 가사 검색

from bisect import bisect_left, bisect_right
# bisect_left(a, x): x가 처음 나오는 위치 반환
# bisect_right(a, x): x보다 큰 값이 처음 나오는 위치

# 각 단어를 길이에 따라 나눈 후, 모든 리스트 정렬, 각 쿼리에 대해 이진 탐색 수행
# 접두사에 와일드카드가 등장하면: 뒤집힌 단어 리스트 대상으로 이진 탐색

# 값이 [left_value, right_value]인 데이터 개수 반환
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_right(a, left_value)
    return right_index - left_index


# 모든 단어를 길이마다 나눠 저장
array = [[] for _ in range(10001)]
# 뒤집어 저장
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):  # 이진 탐색 수행 위해 정렬
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:  # 쿼리 하나씩 확인
        if q[0] != '?':  # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z')) # '?'를 'a'로 바꾸면 가장 작은 문자, 'z'로 바꾸면 가장 큰 문자가 되어 이진 탐색 범위 설정
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer