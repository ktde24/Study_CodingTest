# 볼링공 고르기
# A, B 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다. 볼링공은 총 N개가 있으며, 같은 무게의 공이라도 서로 다른 공으로 간주
# 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공 개수 카운트
    array[x] += 1

res = 0
for i in range(1, m+1): # 1부터 m까지의 각 무게에 대해
    n -= array[i] # 무게가 i인 볼링공의 개수 제외
    res += array[i] * n

print(res)