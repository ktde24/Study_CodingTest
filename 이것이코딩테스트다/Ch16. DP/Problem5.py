# 못생긴 수
# 못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미. 1은 못생긴 수
# n번째 못생긴 수를 찾는 프로그램 작성

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0 # i2 : 2를 곱해 줄 위치를 가리키는 인덱스
# 처음에 곱셈값 초기화
next2, next3, next5 = 2, 3, 5 # 현재 포인터가 가리키는 못생긴 수에 각각 2, 3, 5를 곱한 결과

# 1부터 n까지 못생긴 수 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중 가장 작은 수 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스 따라 곱셈 결과 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])