# round(반올림하고 싶은 숫자, 반올림하고 출력할 자리수)
# 단, 소수점 뒤가 0으로 끝난다면 :.2f로 자리 정해주지 않으면 .0으로만 나온다
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    d = float(sys.stdin.readline())
    print("${:.2f}".format(round(d*0.8, 2)))