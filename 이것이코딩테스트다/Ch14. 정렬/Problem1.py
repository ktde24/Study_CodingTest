# 국영수(https://www.acmicpc.net/problem/10825)
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

n = int(input())
students = []

# 모든 학생 정보
for _ in range(n):
    students.append(input().split())

# 두 번째 원소 기준 내림차순
# 세 번째 원소 기준 오름차순
# 네 번째 원소 기준 내림차순
# 첫 번째 원소 기준 오름차순
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])