from collections import deque
import sys
N, M, K = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = []
for _ in range(N):
    a.append(list(map(int, list(sys.stdin.readline().rstrip()))))
q = deque()
q.append((0, 0, 0))
d = [[[0]*11 for _ in range(1000)] for _ in range(1000)]
d[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if a[nx][ny]==0 and d[nx][ny][z]==0:
            d[nx][ny][z] = d[x][y][z] + 1
            q.append((nx, ny, z))
        elif z+1<=K and a[nx][ny]==1 and d[nx][ny][z+1]==0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx, ny, z+1))
ans = -1
for i in range(K+1):
    if d[N-1][M-1][i]==0:
        continue
    if ans==-1 or ans>d[N-1][M-1][i]:
        ans = d[N-1][M-1][i]
print(ans)