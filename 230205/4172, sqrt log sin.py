from math import *
import sys
lst = [1] * 1000001
for i in range(1, 1000001):
    # 아래 4개의 함수는 math에서 돌아간다
    # floor : 실수의 소수점 이하 부분을 내림하여 정수로 출력
    # sqrt : 루트
    # log : ln
    # sin : sin함수
    lst[i] = (lst[floor(i-sqrt(i))] + lst[floor(log(i))] + lst[floor(i*sin(i)*sin(i))]) % 1000000
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    print(lst[n])