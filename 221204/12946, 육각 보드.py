def dfs(x, y, c):
    global ans
    color[x][y] = c
    ans = max(ans, 1)
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<n and a[nx][ny]=='X':
            if color[nx][ny] == -1:
                dfs(nx, ny, 1-c)
            ans = max(ans, 2)
            if color[nx][ny] == c:
                ans = max(ans, 3)

import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = [input() for _ in range(n)]
color = [[-1]*n for _ in range(n)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]
ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j]=='X' and color[i][j]==-1:
            dfs(i, j, 0)
print(ans)