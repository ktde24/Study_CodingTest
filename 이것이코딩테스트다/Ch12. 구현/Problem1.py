# 럭키 스트레이트
# '럭키 스트레이트' 기술은 점수가 특정 조건을 만족할 때만 사용 가능
# 특정 조건: 현재 캐릭터의 점수를 N이라고 할 때, 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일
# 현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램 작성

N = input()
len = len(N)
res = 0

# 왼쪽 부분
for i in range(len//2):
    res += int(N[i])

# 오른쪽 부분
for i in range(len//2, len):
    res -= int(N[i])

if res == 0:
    print("LUCKY")
else:
    print("READY")