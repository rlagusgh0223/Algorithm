def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W and ground[nx][ny]=='#':
                q.append((nx, ny))
                ground[nx][ny] = '*'

from collections import deque
import sys
T = int(sys.stdin.readline())
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
for i in range(T):
    H, W = map(int, sys.stdin.readline().split())
    ground = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if ground[i][j] == '#':
                cnt += 1
                bfs(i, j)
    print(cnt)