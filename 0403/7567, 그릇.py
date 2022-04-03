import sys
str = list(sys.stdin.readline().rstrip())
n = 10    # 일단 처음 놓이는 접시는 무조건 10cm이므로 10으로 시작
for i in range(1, len(str)):    # 처음 접시의 값은 계산했으므로 2번째 접시부터 계산
    if str[i-1] == str[i]:    # 만약 앞의 접시와 같은 방향이라면
        n += 5    # 5cm 증가
    else:    # 앞의 접시와 다른 방향이라면
        n += 10    # 10cm 증가

print(n)    # 접시의 최종 높이 출력