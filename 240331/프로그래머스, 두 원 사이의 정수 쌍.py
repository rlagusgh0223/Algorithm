# from math import sqrt
# def solution(r1, r2):
#     answer = 0
#     for i in range(r1):
#         answer += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
#     for i in range(r1, r2):
#         answer += int(sqrt(r2**2 - i**2))
#     return answer * 4




# 아래 방법이 더 빠르다
import math


def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        if i < r1:
            # math.ceil : 주어진 숫자보다 큰 수 중 가장 작은수
            # math.sqrt : 제곱근
            s = math.ceil(math.sqrt(r1*r1 - i*i))
        else:
            s = 0
        e = int(math.sqrt(r2*r2 - i*i))
        answer += e - s + 1

    # 위의 식으로는 한 사분면의 값만 구하게 되므로
    # 4사분면의 값을 구하기 위해 4를 곱한다
    return answer*4

import sys

r1, r2 = map(int, sys.stdin.readline().split())
print(solution(r1, r2))