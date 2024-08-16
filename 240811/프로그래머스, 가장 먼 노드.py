from collections import deque


def solution(n, edge):
    load = [[] for _ in range(n+1)]
    check = [-1] * (n+1)
    for x, y in edge:
        load[x].append(y)
        load[y].append(x)
    
    check[1] = 0
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        for nx in load[x]:
            if check[nx] == -1:
                check[nx] = check[x] + 1
                q.append(nx)
                
    return check.count(max(check))

import sys

n = int(sys.stdin.readline())
edge = list(sys.stdin.readline().strip().split("], ["))
edge = [list(map(int, e.split(", "))) for e in edge]
print(solution(n, edge))