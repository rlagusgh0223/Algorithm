import math


def solution(k, d):
    answer = 0
    # x를 기준으로 y값 구하기
    # k=2, d=4라면
    # x가 0일때 y는 0, 2, 4가 되고
    # x가 2일때 y는 0, 2가 되고
    # x가 4일때 y는 0이 된다
    for x in range(0, d+1, k):
        searchY = math.floor(math.sqrt(d*d - x*x))
        answer += (searchY//k) + 1
    return answer

import sys

k, d = map(int, sys.stdin.readline().split())
print(solution(k, d))
