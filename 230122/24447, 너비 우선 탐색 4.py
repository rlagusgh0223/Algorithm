def bfs(r):
    q = deque()
    q.append(r)
    d[r] += 1
    t[r] = 1
    cnt = 1
    ans = 0
    while q:
        x = q.popleft()
        for nx in lst[x]:
            if t[nx]==0:
                cnt += 1
                t[nx] = cnt
                d[nx] = d[x] + 1
                q.append(nx)
    for i in range(N):
        ans += d[i]*t[i]
    return ans

from collections import deque
import sys
N, M, R = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N)]
d = [-1] * N
t = [0] * N
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    lst[u].append(v)
    lst[v].append(u)
for i in range(N):
    lst[i].sort()
print(bfs(R-1))