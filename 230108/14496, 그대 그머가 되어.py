def bfs():
    q = deque()
    q.append(a)
    ck[a] = 1
    while q:
        x = q.popleft()
        if x == b:
            return ck[x]-1
        for now in lst[x]:
            if ck[now] == 0:
                ck[now] = ck[x] + 1
                q.append(now)
    return -1

from collections import deque
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
N, M = map(int, input().split())
lst = [[] for i in range(N+1)]
ck = [0]*(N+1)
for i in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
print(bfs())