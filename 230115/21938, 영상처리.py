def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and color2[nx][ny]==255 and check[nx][ny]==0:
                check[nx][ny] = 1
                q.append((nx, ny))

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
color2 = [[0]*M for _ in range(N)]
check = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        cnt = color[i][j*3] + color[i][j*3+1] + color[i][j*3+2]
        if cnt//3 >= T:
            color2[i][j] = 255
        else:
            color2[i][j] = 0
ans = 0
for i in range(N):
    for j in range(M):
        if color2[i][j]==255 and check[i][j]==0:
            ans += 1
            check[i][j] = 1
            bfs(i, j)
print(ans)