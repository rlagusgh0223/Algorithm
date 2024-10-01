def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(w, h):
    # 전체 사각형 개수에서 대각선이 지나는 사각형의 개수를 뺌
    return w*h - (w+h - GCD(w, h))

import sys

w = int(sys.stdin.readline())
h = int(sys.stdin.readline())
print(solution(w, h))