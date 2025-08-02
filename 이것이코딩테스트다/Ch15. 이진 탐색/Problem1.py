# 정렬된 배열에서 특정 수의 개수 구하기
# N, x가 공백으로 구분되어 ㅇ비력
# N개의 원소가 정수 형태로 공백으로 구분되어 입력
# 수열의 원소 중에서 값이 x인 원소의 개수 출력, 하나도 없으면 -1 출력

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터 개수
    n = len(array)
    # x가 처음 등장하는 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 X
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개

    # x가 마지막으로 등장하는 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수 반환
    return b-a+1

# 처음 위치 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid+1, end)

# 마지막 위치 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == len(array) - 1 or array[mid + 1] > target) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split())) # 전체 데이터 입력

# 값이 x인 데이터 개수
cnt = count_by_value(array, x)
# x인 원소가 존재하지 않으면
if cnt == 0:
    print(-1)
else:
    print(cnt)