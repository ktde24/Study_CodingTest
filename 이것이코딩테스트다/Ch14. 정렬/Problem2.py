# 안테나(https://www.acmicpc.net/problem/18310

N = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값
print(data[(N-1) // 2])