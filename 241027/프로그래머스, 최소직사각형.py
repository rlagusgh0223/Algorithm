def solution(sizes):
    w, h = [], []
    for size in sizes:
        x, y = max(size), min(size)
        w.append(x)
        h.append(y)
    return max(w) * max(h)

import sys

sizes = list(sys.stdin.readline().strip().split("], ["))
sizes = [list(map(int, s.split(", "))) for s in sizes]
print(solution(sizes))