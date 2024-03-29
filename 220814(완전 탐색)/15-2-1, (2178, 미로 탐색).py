from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
q = deque()
q.append([0, 0])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.append([nx, ny])

print(maze[N-1][M-1])