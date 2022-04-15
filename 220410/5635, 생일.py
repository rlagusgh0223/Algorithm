import sys
n = int(sys.stdin.readline())
lst = []
young = 0    # 어린 사람이 몇번째인지 카운트하는 변수
old = 0    # 나이 많은 사람이 몇번째인지 카운트하는 변수

for i in range(n):
    lst.append(list(sys.stdin.readline().split()))    # 학생의 이름도 받으므로 int로 받을 수 없다
    lst[i][1] = int(lst[i][1])
    lst[i][2] = int(lst[i][2])
    lst[i][3] = int(lst[i][3])

year = 1989    # 연도를 비교하는 변수. 나이가 많은 사람을 찾으므로 1989년을 입력한다(연도 입력 범위 1990 ~ 2010)
month = 0    # 월을 비교하는 변수
day = 0    # 날짜를 비교하는 변수
for i in range(n):    # 나이가 적은 사람을 구하는 반복문
    if year < lst[i][3]:    # 연도가 작다면 다른건 볼 필요도 없이 나이가 어린것이니 어린사람의 날짜로 바꾼다
        year = lst[i][3]
        month = lst[i][2]
        day = lst[i][1]
        young = i
    elif year == lst[i][3] and month < lst[i][2]:    # 태어난 해는 같아도 월이 더 빠른 경우
        month = lst[i][2]    # 연도는 어차피 같으므로 값 줄 필요 없다
        day = lst[i][1]
        young = i
    elif year == lst[i][3] and month == lst[i][2] and day < lst[i][1]:
        day = lst[i][1]
        young = i

year = 2011    # 연도를 비교하는 변수. 처음에는 가장 어린 사람을 찾으므로 이렇게 초기화(입력 범위는 2010년이다)
month = 13
day = 32
for i in range(n):    # 나이가 많은 사람을 구하는 반복문
    if year > lst[i][3]:    # 연도가 크다면 다른건 볼 필요도 없이 나이가 많은것이니 많은사람의 날짜로 바꾼다
        year = lst[i][3]
        month = lst[i][2]
        day = lst[i][1]
        old = i
    elif year == lst[i][3] and month > lst[i][2]:    # 태어난 해는 같아도 월이 더 느린 경우
        month = lst[i][2]    # 연도는 어차피 같으므로 값 줄 필요 없다
        day = lst[i][1]
        old = i
    elif year == lst[i][3] and month == lst[i][2] and day > lst[i][1]:
        day = lst[i][1]
        old = i

print(lst[young][0])
print(lst[old][0])