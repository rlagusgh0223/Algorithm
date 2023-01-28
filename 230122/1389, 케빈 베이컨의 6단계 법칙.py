def bfs(x):
    q = deque()
    q.append(x)
    ck = [-1] * N
    ck[x] = 0
    while q:
        x = q.popleft()
        for nx in f[x]:
            if ck[nx] == -1:
                ck[nx] = ck[x] + 1
                q.append(nx)
    lst.append(sum(ck))

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
f = [[] for _ in range(N)]
lst = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    A-=1
    B-=1
    f[A].append(B)
    f[B].append(A)
for i in range(N):
    bfs(i)
print(lst.index(min(lst))+1)