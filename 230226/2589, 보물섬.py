# pypy3로 돌려야 된다
def BFS(x, y):
    q = deque()
    q.append((x, y))
    value[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and island[nx][ny]=='L' and value[nx][ny]==-1:
                q.append((nx, ny))
                value[nx][ny] = value[x][y] + 1
    return max(map(max, value))

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
island = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            value = [[-1]*m for _ in range(n)]
            ans = max(ans, BFS(i, j))
print(ans)