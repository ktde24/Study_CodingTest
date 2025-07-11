# 곱하기 혹은 더하기
# 각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수 출력
# 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정

data = input()

# 첫 문자를 숫자로 변경해서 대입
res = int(data[0])

for i in range(1, len(data)):
    # 두 수 중 하나라도 0이나 1이면 더하기
    num = int(data[i])
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num
print(res)