def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and ground[nx][ny]==ground[x][y] and visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = False

from collections import deque
import sys
N = int(sys.stdin.readline())
ground = []
for i in range(N):
    ground.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
no = yes = 0
visit = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            bfs(i, j)
            no += 1
for i in range(N):
    for j in range(N):
        if ground[i][j] == "G":
            ground[i][j] = "R"
visit = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            bfs(i, j)
            yes += 1
print(no, yes)