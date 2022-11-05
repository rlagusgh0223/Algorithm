def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    lst[a][b] = 1
    while q:
        x, y = q.popleft()
        if x==c and y==d:
            print(lst[x][y] - 1)
            return
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and lst[nx][ny]==0:
                lst[nx][ny] = lst[x][y] + 1
                q.append((nx, ny))

from collections import deque
import sys
T = int(sys.stdin.readline())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
for i in range(T):
    l = int(sys.stdin.readline())
    lst = [[0]*l for _ in range(l)]
    x, y = map(int, sys.stdin.readline().split())
    nx, ny = map(int, sys.stdin.readline().split())
    bfs(x, y, nx, ny)