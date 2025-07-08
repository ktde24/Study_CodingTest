# 효율적인 화폐 구성
# N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# M원을 만들기 위한 최소한의 화폐 개수 출력, 불가능할 때는 -1 출력

# 점화식
# a_i-k를 만드는 방법이 존재: ai = min(ai, a_i-k+1)
# a_i-k를 만드는 방법이 존재 X: ai = 10001

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-arr[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])