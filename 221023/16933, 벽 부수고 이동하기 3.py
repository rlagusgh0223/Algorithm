# 메모리 초과
from collections import deque
a = [[0]*1000 for _ in range(1000)]
d = [[[[0]*2 for k in range(11)] for i in range(1000)] for j in range(1000)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m, l = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, list(input()))))
q = deque()
d[0][0][0][0] = 1
q.append((0, 0, 0, 0))
while q:
    x, y, z, night = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if a[nx][ny]==0 and d[nx][ny][z][1-night]==0:
            d[nx][ny][z][1-night] = d[x][y][z][night]+1
            q.append((nx, ny, z, 1-night))
        if night==0 and z+1<=l and a[nx][ny]==1 and d[nx][ny][z+1][1-night]==0:
            d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1
            q.append((nx, ny, z+1, 1-night))
    if d[x][y][z][1-night]==0:
        d[x][y][z][1-night] = d[x][y][z][night]+1
        q.append((x, y, z, 1-night))
ans = -1
for j in range(2):
    for i in range(l+1):
        if d[n-1][m-1][i][j]==0:
            continue
        if ans == -1:
            ans = d[n-1][m-1][i][j]
        elif ans > d[n-1][m-1][i][j]:
            ans = d[n-1][m-1][i][j]
print(ans)