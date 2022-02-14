import sys

d = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]    # 문제에서 주어진 리스트
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    if n > len(d):    # n이 이미 있는 리스트 안에 있다면 따로 구할 필요 없지만 리스트 값을 넘는다면 새로 구해야 한다
        while n > len(d):    # n개의 리스트가 될때까지 반복
            d.append(d[len(d)-1] + d[len(d)-5])    # 점화식 d[i] = d[i-1] + d[i-5]
    print(d[n-1])    # n번째의 리스트 출력