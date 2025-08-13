# 퇴사(https://www.acmicpc.net/problem/14501)
# 뒤쪽부터 매 상담에 대해 현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대이윤
# dp[i]: i번째 날부터 마지막날까지 낼 수 있는 최대 이익

n = int(input())
t = [] # 각 상담을 완료하는데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # 1차원 dp 테이블
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간 벗어나면
    else:
        dp[i] = max_value
print(max_value)