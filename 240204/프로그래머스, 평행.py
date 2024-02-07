# 두 점 사이의 기울기 구하는 공식
# y축의 차 / x축의 차
def grad(a, b):
    return (b[1]-a[1]) / (b[0]-a[0])

def solution(dots):
    p1, p2, p3, p4 = dots[:4]
    if grad(p1,p2)==grad(p3,p4) or grad(p1,p3)==grad(p2,p4) or grad(p1,p4)==grad(p2,p3):
        return 1
    return 0

import sys
dots = list(sys.stdin.readline().strip().split("], ["))
dots = [list(map(int, dot.split(", "))) for dot in dots]
print(solution(dots))