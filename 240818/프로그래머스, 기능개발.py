import math


def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        ps = math.ceil((100-p) / s)
        if not answer or answer[-1][0]<ps:
            answer.append([ps, 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]

import sys

p = list(map(int, sys.stdin.readline().split(", ")))
s = list(map(int, sys.stdin.readline().split(", ")))
print(solution(p, s))