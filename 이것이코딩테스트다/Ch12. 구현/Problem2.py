# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력

S = input()
res = []
val = 0

# 문자를 하나씩 확인
for i in S:
    # 알파벳이면 리스트에 삽입
    if i.isalpha():
        res.append(i)
    else:
        val += int(i)

res.sort() # 알파벳 정렬

# 숫자가 하나라도 존재하면 가장 뒤에
if val != 0:
    res.append(str(val))

print(''.join(res)) # 리스트를 문자열로 변환하여 출력