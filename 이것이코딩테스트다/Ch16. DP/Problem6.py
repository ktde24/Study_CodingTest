# 편집 거리
# 두 개의 문자열 A, B가 주어졌을 때, 문자열 A를 편집하여 B로 만들고자 한다.
# 삽입, 삭제, 교체 중 하나씩 선택하여 이용 가능
# 문자열 A를 B로 만드는 최소 편집 거리를 계산하는 프로그램 작성

# 두 문자가 같은 경우: dp[i][j] = dp[i-1[j-1] => 행과 열에 해당하는 문자가 서로 같으면, 왼쪽 위에 해당하는 수 그대로 대입
# 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1[j-1]) => 다르면, 삽입/삭제/교체 중 가장 작은수에 1 더해서 대입

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j


    # 최소 편집 거리
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르면
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]


str1 = input()
str2 = input()

print(edit_dist(str1, str2))
