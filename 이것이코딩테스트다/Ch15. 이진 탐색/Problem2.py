# 고정점 찾기
# 고정점이란, 수열의 원소 중 그 값이 인덱스와 동일한 원소를 의미. 하나의 수열이 N개의 서로 다르 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있을 때
# 이 수열에서 고정점이 있다면 고정점을 출력하는 프로그램 작성. 없으면 -1 출력
# 시간 복잡도 O(logN)으로 알고리즘 설계

# 이진 탐색
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)


N = int(input())
array = list(map(int, input().split()))
index = binary_search(array, 0, N-1)

if index == None:
    print(-1)
else:
    print(index)