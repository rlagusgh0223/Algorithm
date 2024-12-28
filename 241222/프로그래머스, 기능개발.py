import math


def solution(progresses, speeds):
    answer = [[0, 0]]
    for p, s in zip(progresses, speeds):
        now = math.ceil((100-p) / s)
        if answer[-1][0] < now:
            answer.append([now, 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer[1:]]

import sys

p = list(map(int, sys.stdin.readline().split(", ")))
s = list(map(int, sys.stdin.readline().split(", ")))
print(solution(p, s))