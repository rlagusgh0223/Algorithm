def bfs():
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and ground[nx][ny] == 0:
                ground[nx][ny] = ground[x][y] + 1
                q.append((nx, ny))
                if cnt < ground[nx][ny]:
                    cnt = ground[nx][ny]
    return cnt-1  # 1이 아기상어이므로 거리를 2부터 시작했다. 1을 빼서 거리를 정확하게 맞춰준다

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
q = deque()
for i in range(N):
    for j in range(M):
        if ground[i][j] == 1:
            q.append((i, j))
print(bfs())