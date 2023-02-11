# 2015년 9월 17일에 사귄다는 말은 왜 썼는지 모르겠다
# 그냥 2014년 4월 2일을 기준으로 입력된 수 만큼 지날날을 출력하면 된다
import sys
N = int(sys.stdin.readline())
yun = [x for x in range(2014, 2045) if x%400==0 or (x%4==0 and x%100!=0)]
Y = 2014
M = 4
D = 1
for _ in range(N):
    if M in [1, 3, 5, 7, 8, 10] and D==31:
        M += 1
        D = 1
    elif M in [4, 6, 9, 11] and D==30:
        M += 1
        D = 1
    elif M==12 and D==31:
        Y += 1
        M = 1
        D = 1
    elif M == 2:
        if Y in yun and D==29:
            M += 1
            D = 1
        elif Y not in yun and D==28:
            M += 1
            D = 1
        else:
            D += 1
    else:
        D += 1
print("{}-{:02d}-{:02d}".format(Y, M, D))