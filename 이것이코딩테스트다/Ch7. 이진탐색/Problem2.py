# 부품 찾기
# 부품이 N개 있음. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 견적서 요청.
# 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 함.

# 각 부품이 존재하면 yes, 없으면 no 출력

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 입력
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split())) # 손님이 요청한 부품 번호

for i in x:
    res = binary_search(array, i, 0, n-1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')