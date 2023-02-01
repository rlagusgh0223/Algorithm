def bfs(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    road[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and road[nx][ny]==-1:
                road[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt

from collections import deque
import sys
N, M ,K = map(int, sys.stdin.readline().split())
road = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    road[x][y] = -1
for i in range(N):
    for j in range(M):
        if road[i][j] == -1:
            ans = max(ans, bfs(i, j))
print(ans)