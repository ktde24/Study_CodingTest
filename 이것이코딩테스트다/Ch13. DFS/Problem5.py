# 연산자 끼워 넣기(https://www.acmicpc.net/problem/14888)

N = int(input())
data = list(map(int, input().split())) # 연산 수행하고자 하는 리스트
add, sub, mul, div = map(int, input().split()) # 연산자 개수

min_value = 1e9
max_value = -1e9

# DFS 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1

        if div > 0:
            div -= 1
            # 문제 조건에 맞는 나눗셈 처리
            if now < 0:
                dfs(i + 1, -(-now // data[i]))
            else:
                dfs(i + 1, now // data[i])
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)