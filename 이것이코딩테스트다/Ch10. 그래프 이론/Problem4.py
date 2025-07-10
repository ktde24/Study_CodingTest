# 커리큘럼
# 동빈이가 듣고자 하는 강의수 N이 주어짐. 각 강의의 시간, 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어짐
# N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

from collections import deque
import copy

# 노드 개수 입력
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 간선 정보 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    res = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            res[i] = max(res[i], res[now] + time[i])
            indegree[i] -= 1
            # 새롭게 ㅇ진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v+1):
        print(res[i])

topology_sort()