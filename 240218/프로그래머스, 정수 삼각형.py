# 아래에서 위로 올라가면서 더 큰 값을 더하면 마지막엔 가장 큰 값이 나온다
def solution(triangle):
    floor = len(triangle) - 1
    while floor > 0:
        for i in range(floor):
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1
    return triangle[0][0]

import sys

t = list(sys.stdin.readline().strip().split("], ["))
t = [list(map(int, now.split(", "))) for now in t]
print(solution(t))