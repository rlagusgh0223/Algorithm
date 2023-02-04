def BFS():
    q = deque()
    q.append(1)
    ck[1] = 0
    while q:
        x = q.popleft()
        for nx in lst[x]:
            if ck[nx] == -1:
                ck[nx] = ck[x] + 1
                q.append(nx)

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
ck = [0] + [-1]*N
lst = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)
BFS()
print(ck.index(max(ck)), ck[ck.index(max(ck))], ck.count(max(ck)))