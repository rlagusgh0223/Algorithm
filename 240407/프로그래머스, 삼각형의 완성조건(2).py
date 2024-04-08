def solution(sides):
    # 구해야 될 n이 가장 긴 경우
    # max(sides) + min(sides) > n 이어야 하고
    # n이 가장 길지 않은 경우
    # min(sides) + n > max(sides) 여야 한다
    return sum(sides) - (max(sides) - min(sides)) - 1

import sys

print(solution(list(map(int, sys.stdin.readline().split(', ')))))
