from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and check[nx][ny]==0:
                check[nx][ny] = 1
                q.append((nx, ny))

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
yes = no = 0
check = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(N):
        if check[i][j]==0:
            bfs(i, j)
            yes += 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
check = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if check[i][j]==0:
            bfs(i, j)
            no += 1
print(yes, no)