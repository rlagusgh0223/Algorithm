# 모범답안
def solution(sizes):
    return max([max(s) for s in sizes]) * max([min(s) for s in sizes])

# def solution(sizes):
#     w, h = [], []
#     for size in sizes:
#         w.append(max(size))
#         h.append(min(size))
#     return max(w) * max(h)

import sys

sizes = list(sys.stdin.readline().strip().split("], ["))
sizes = [list(map(int, s.split(", "))) for s in sizes]
print(solution(sizes))