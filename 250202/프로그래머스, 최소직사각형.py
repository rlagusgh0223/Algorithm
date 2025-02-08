def solution(sizes):
    Max, Min = [], []
    for size in sizes:
        Max.append(max(size))
        Min.append(min(size))
    return max(Max) * max(Min)

import sys

sizes = list(sys.stdin.readline().strip().split("], ["))
sizes = [list(map(int, s.split(", "))) for s in sizes]
print(solution(sizes))