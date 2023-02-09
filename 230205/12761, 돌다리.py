def BFS(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x+dx[i]
            else:
                nx = x*dx[i]
            if 0<=nx<100001 and ck[nx]==0:
                ck[nx] = 1
                q.append(nx)
                lst[nx] = lst[x] + 1
            if nx == M:
                break

from collections import deque
import sys
A, B, N, M = map(int, sys.stdin.readline().split())
lst = [0] * 100001
ck = [0] * 100001
dx = [1, -1, A, B, -A, -B, A, B]
BFS(N)
print(lst[M])