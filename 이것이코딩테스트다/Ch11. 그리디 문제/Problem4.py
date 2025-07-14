# 만들 수 없는 금액
# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램 작성

# 화폐 단위 기준으로 오름차순 정렬
# 1부터 특정 금액을 만들 수 있는지 확인

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액 찾으면 종료
    if target < x:
        break
    target += x

print(target)