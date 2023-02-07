def BFS(i, j):
    q = deque()
    q.append((i, j))
    ground[i][j] = 0
    check[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and ground[nx][ny]==1 and check[nx][ny]==0:
                ground[nx][ny] = ground[x][y] + 1
                check[nx][ny] = 1
                q.append((nx, ny))

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if ground[i][j]==2 and check[i][j]==0:
            BFS(i, j)
for i in range(n):
    for j in range(m):
        if check[i][j]==0 and ground[i][j]==1:
            ground[i][j] = -1
for i in range(n):
    print(*ground[i])