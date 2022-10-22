from collections import deque
import sys
N = int(sys.stdin.readline())
ground = [[-1 for _ in range(N)] for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
q = deque()
q.append((r1, c1))
ground[r1][c1] = 0
while q:
    x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and ground[nx][ny] == -1:
            ground[nx][ny] = ground[x][y] + 1
            q.append((nx, ny))
print(ground[r2][c2])