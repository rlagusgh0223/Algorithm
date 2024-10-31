import math


def solution(slice, n):
    # return (n-1)//slice + 1  # 모범답안
    return math.ceil(n/slice)

import sys

s, n = map(int, sys.stdin.readline().split())
print(solution(s, n))