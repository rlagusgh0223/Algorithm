def solution(sizes):
    w, h = [], []
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    return max(w) * max(h)

import sys

sizes = list(sys.stdin.readline().split("], ["))
sizes = [list(map(int, s.split(", "))) for s in sizes]
print(solution(sizes))