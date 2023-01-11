def bfs():
    q = deque()
    q.append(R)
    cnt = 1
    ck[R] = 1
    while q:
        x = q.popleft()
        Num[x].sort()
        for now in Num[x]:
            if ck[now] == 0:
                q.append(now)
                cnt += 1
                ck[now] = cnt

from collections import deque
import sys
N, M, R  = map(int, sys.stdin.readline().split())
ck = [0] * (N+1)
Num = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    Num[x].append(y)
    Num[y].append(x)

bfs()
for now in ck[1:]:
    print(now)