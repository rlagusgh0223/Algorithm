N = int(input())    # N개의 정수 입력
lst = [int(now) for now in input().split()]    # 정수 입력

cnt = 0     # 정수의 순서를 측정하기 위한 변수 선언
Max = lst[0]    # 최댓값을 기록할 변수
Min = lst[0]    # 최솟값을 기록할 변수

for i in range(1, N):    # 두번째 수부터 끝까지(첫번째 수는 이미 입력함)
    if Max < lst[i]:    # 현재 최댓값이 현재값보다 작다면
        Max = lst[i]    # 현재 최댓값 수정
    elif Min > lst[i]:    # 현재 최솟값이 현재값보다 크다면
        Min = lst[i]    # 현재 최솟값 수정

print(Min, Max)    # 최솟값, 최댓값 출력