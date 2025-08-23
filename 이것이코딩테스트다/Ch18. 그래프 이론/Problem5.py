# 최종 순위(https://www.acmicpc.net/problem/3665)
# 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만드는 프로그램 작성
# 확실한 올해 순위를 만들 수 업슨 경우, 일관성이 없는 잘못된 정보일 수도 있음

# 정해진 우선순위에 맞게 전체 팀들의 순서 나열 => 위상 정렬 알고리즘
# 팀 간의 순위 정보를 그래프 정보로 표현(자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프 만들기)
# 특수 케이스: 사이클이 발생하는 경우, 위상 정렬의 결과가 여러가지인 경우 => 노드가 N번 나오기 전에 큐가 비게 됨 or 특정 시점에 2개 이상의 노드가 큐에 한번에 들어감

import sys
from collections import deque

input = sys.stdin.readline

# 아이디어 요약
# 1) 작년 순위가 "완전한 순서"이므로, 높은 팀 -> 낮은 팀으로 향하는 방향 그래프를 만든다.
# 2) 올해 바뀐 상대 순위 쌍 (a, b)를 입력받을 때마다 a<->b 간선의 방향을 반대로 바꾸고,
#    그에 따라 두 정점의 진입차수(indegree)도 즉시 갱신한다.
# 3) 이후 Kahn의 위상 정렬을 수행.
#    - 큐에 indegree 0인 노드가 "동시에 2개 이상" 들어간 적이 있으면 결과가 여러 개가 될 수 있으므로 '?'
#    - 위상 정렬 중 큐가 비어 "n개를 모두 뽑기 전에" 멈추면 사이클이 존재하므로 'IMPOSSIBLE'
#    - 둘 다 아니면 단 한 가지 정답이 확정되므로 그 순서를 출력

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())

    # indegree[i]: 정점 i의 현재 진입차수
    indegree = [0] * (n + 1)

    # 인접행렬(graph[u][v] == True 이면 u -> v 방향 간선 존재)
    # n ≤ 500 이므로 인접행렬 사용 가능
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 작년 순위(앞에 있을수록 더 높은 순위)
    last = list(map(int, input().split()))

    # 1) 작년 순위 기반으로 "완전 DAG" 구성
    # last = [t1, t2, ..., tn] 이면
    # t1 -> t2, t1 -> t3, ..., t1 -> tn
    # t2 -> t3, ..., t2 -> tn
    for i in range(n):
        higher = last[i]
        for j in range(i + 1, n):
            lower = last[j]
            if not graph[higher][lower]:
                graph[higher][lower] = True
                indegree[lower] += 1

    # 올해 바뀐 상대 순위 정보 M
    m = int(input().strip())

    for _chg in range(m):
        a, b = map(int, input().split())
        # a -> b 가 있었다면 b -> a 로 뒤집는다
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        # 반대로 b -> a 가 있었다면 a -> b 로 뒤집는다
        elif graph[b][a]:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1
        else:
            # 이 경우는 입력 전제상 발생하지 않지만,
            # 안전 차원에서 처리(간선이 반드시 한 쪽 방향으로 존재해야 함)
            # 간선이 없었으면 새로 만든다고 가정
            graph[a][b] = True
            indegree[b] += 1

    # 2) 위상 정렬(Kahn)
    q = deque([i for i in range(1, n + 1) if indegree[i] == 0])

    result = []
    ambiguous = False  # 어떤 시점에 indegree 0 노드가 2개 이상이면 True
    impossible = False  # 중간에 큐가 비면(사이클) True

    for _pick in range(n):
        if not q:
            # n개를 다 뽑기 전에 큐가 비면 사이클 존재
            impossible = True
            break

        if len(q) > 1:
            # 정답이 여러 가지 가능(확정 불가)
            ambiguous = True

        cur = q.popleft()
        result.append(cur)
        # cur에서 나가는 모든 간선 제거(진입차수 감소)
        for nxt in range(1, n + 1):
            if graph[cur][nxt]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

    # 3) 출력 규칙
    if impossible:
        print("IMPOSSIBLE")
    elif ambiguous:
        print("?")
    else:
        print(*result)

