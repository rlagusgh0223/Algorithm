from collections import deque
dx = [-1, 0, 1, 0, -1, -2, -2, -1, 1, 2, 2, 1]
dy = [0, 1, 0, -1, -2, -1, 1, 2, -2, -1, 1, 2]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
K = int(input())
W, H = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
d = [[[-1]*31 for _ in range(200)] for _ in range(200)]
d[0][0][0] = 0
q = deque()
q.append((0, 0, 0))
while q:
    x, y, c = q.popleft()
    for i in range(12):
        nx, ny, nc = x+dx[i], y+dy[i], c+cost[i]
        if 0<=nx<H and 0<=ny<W:
            if a[nx][ny] == 1:
                continue
            if nc <= K:
                if d[nx][ny][nc] == -1:
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx, ny, nc))
ans = -1
for i in range(K+1):
    if d[H-1][W-1][i] == -1:
        continue
    if ans==-1 or ans>d[H-1][W-1][i]:
        ans = d[H-1][W-1][i]
print(ans)