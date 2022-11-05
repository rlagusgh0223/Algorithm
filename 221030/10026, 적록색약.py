def bfs(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and check[nx][ny]:
                check[nx][ny] = False
                q.append((nx, ny))

from collections import deque
import sys
N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
check = [[True]*N for _ in range(N)]
cnt1 = cnt2 = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    for j in range(N):
        if check[i][j]:
            bfs(i, j)
            cnt1 += 1

check = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"
for i in range(N):
    for j in range(N):
        if check[i][j]:
            bfs(i, j)
            cnt2 += 1
print(cnt1, cnt2)