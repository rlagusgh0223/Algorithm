def solution(dots):
    x, y = [dot[0] for dot in dots], [dot[1] for dot in dots]
    X = max(x) - min(x)
    Y = max(y) - min(y)
    return X*Y

import sys

dots = list(sys.stdin.readline().strip().split("], ["))
dots = [list(map(int, d.split(", "))) for d in dots]
print(solution(dots))