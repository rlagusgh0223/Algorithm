from collections import deque
W, H = map(int, input().split())
a = [input() for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sx = sy = ex = ey = -1
for i in range(H):
    for j in range(W):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j
dist = [[-1]*W for i in range(H)]
dist[sx][sy] = 0
q = deque()
q.append((sx, sy))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        while 0<=nx<H and 0<=ny<W:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            nx += dx[i]
            ny += dy[i]
print(dist[ex][ey] - 1)