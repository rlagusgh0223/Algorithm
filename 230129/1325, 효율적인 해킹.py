# pypy3로 풀어야 한다
def bfs(i):
    q = deque()
    q.append(i)
    ck = [-1] * N
    ck[i] = 0
    while q:
        x = q.popleft()
        for nx in h[x]:
            if ck[nx] == -1:
                ck[nx] = 1
                q.append(nx)
    return sum(ck)+1

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
h = [[] for _ in range(N)]
lst = [0] * N
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    h[y-1].append(x-1)
for i in range(N):
    lst[i] = bfs(i)
for i in range(N):
    if lst[i] == max(lst):
        print(i+1, end=' ')
print()