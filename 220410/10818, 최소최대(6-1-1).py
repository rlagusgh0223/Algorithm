import sys
n = int(sys.stdin.readline())    # 정수의 개수 입력
lst = list(map(int, sys.stdin.readline().split()))    # 띄어쓰기를 구분으로 정수 입력
max = lst[0]    # 가장 큰 값을 입력할 변수
min = lst[0]    # 가장 작은 값을 입력할 변수

for i in range(1, n):
    if lst[i] > max:    # 현재 값이 최댓값보다 크다면 최대값에 현재값 입력
        max = lst[i]
    if lst[i] < min:    # 현재 값이 최솟값보다 작다면 최솟값에 현재값 입력
        min = lst[i]

print(min, max)    # 최솟값, 최댓값 출력