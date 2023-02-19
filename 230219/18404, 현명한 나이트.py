def BFS(x, y):
    q = deque()
    q.append((x, y))
    ground[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and ground[nx][ny]==-1:
                q.append((nx, ny))
                ground[nx][ny] = ground[x][y] + 1

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
ground = [[-1]*N for _ in range(N)]
ans = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
BFS(x-1, y-1)
for x, y in ans:
    print(ground[x-1][y-1], end=' ')
print()