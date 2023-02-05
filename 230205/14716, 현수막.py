def BFS(i, j):
    q = deque()
    q.append((i, j))
    pam[i][j] = -1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and pam[nx][ny]==1:
                pam[nx][ny] = -1
                q.append((nx, ny))

from collections import deque
import sys
M, N = map(int, sys.stdin.readline().split())
pam = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
cnt = 0
dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
for i in range(M):
    for j in range(N):
        if pam[i][j] == 1:
            cnt += 1
            BFS(i, j)
print(cnt)