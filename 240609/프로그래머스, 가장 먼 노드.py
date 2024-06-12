from collections import deque


def solution(n, edge):
    visit = [[] for _ in range(n+1)]
    check = [-1] * (n+1)
    for x, y in edge:
        visit[x].append(y)
        visit[y].append(x)
    check[1] = 0
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        for nx in visit[x]:
            if check[nx] == -1:
                q.append(nx)
                check[nx] = check[x] + 1
    return check.count(max(check))

import sys

n = int(sys.stdin.readline())
vertex = list(sys.stdin.readline().strip().split("], ["))
vertex = [list(map(int, v.split(", "))) for v in vertex]
print(solution(n, vertex))