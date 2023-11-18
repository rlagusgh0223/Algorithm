# 돌려서 넣는다는건 명함을 가로/세로로 넣어도 상관없다는 거다
# 그냥 한쪽 면이 더 긴 부분끼리 비교하고, 한쪽 면이 더 짧은 부분끼리 비교하면 된다
def solution(sizes):
    w, h = [], []
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    return max(w) * max(h)

import sys
sizes = list(sys.stdin.readline().strip().split("], ["))
for s in range(len(sizes)):
    sizes[s] = list(map(int, sizes[s].split(", ")))
print(solution(sizes))