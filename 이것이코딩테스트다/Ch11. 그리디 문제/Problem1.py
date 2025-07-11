# 모험가 길드
# 모험가 N명이 있다. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 출력

n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 0
cnt = 0 # 현재 그룹에 포함된 모함가 수

for i in data:
    cnt += 1 # 현재 그룹에 해당 모험가 포함
    if cnt >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면, 그룹 결성
        res += 1
        cnt = 0 # 현재 그룹에 포함된 모험가 수 초기화

print(res)