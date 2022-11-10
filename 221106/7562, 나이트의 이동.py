def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    ground[a][b] = 1
    while q:
        x, y = q.popleft()
        if x==c and y==d:
            print(ground[x][y] - 1)
            return
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and ground[nx][ny]==0:
                q.append((nx, ny))
                ground[nx][ny] = ground[x][y] + 1

from collections import deque
import sys
N = int(sys.stdin.readline())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
for i in range(N):
    l = int(sys.stdin.readline())
    ground = [[0]*l for _ in range(l)]
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())
    bfs(x1, y1, x2, y2)