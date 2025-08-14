# 병사 배치하기(https://www.acmicpc.net/problem/18353)

# 가장 긴 증가하는 부분 수열(하나의 수열이 주어졌을 때, 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제)의 아이디어와 동일
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n # 1차원 DP 테이블

# 가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(n-max(dp))