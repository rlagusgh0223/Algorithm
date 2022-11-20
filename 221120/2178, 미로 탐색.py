def bfs():
    q = deque()
    q.append((0, 0))
    maze[0][0] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
    return maze[N-1][M-1]-1

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
maze = []
for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(bfs())