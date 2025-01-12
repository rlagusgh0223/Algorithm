from collections import deque


def solution(n, edge):
    way = [[] for _ in range(n+1)]
    check = [-1] * (n+1)
    for x, y in edge:
        way[x].append(y)
        way[y].append(x)
    q = deque()
    q.append(1)
    check[1] = 0
    while q:
        x = q.popleft()
        for y in way[x]:
            if check[y] == -1:
                check[y] = check[x] + 1
                q.append(y)

    return check.count(max(check))

import sys

n = int(sys.stdin.readline())
edgy = list(sys.stdin.readline().strip().split('], ['))
edgy = [list(map(int, e.split(", "))) for e in edgy]
print(solution(n, edgy))