from collections import deque
import sys
dx = [0, 1, 0, -1, 1, 1, -1, -1, 0]
dy = [1, 0, -1, 0, 1, -1, 1, -1, 0]
q = deque()
q.append((7, 0, 0))
n = 8
ground = [sys.stdin.readline().rstrip() for _ in range(n)]
check = [[[False]*(n+1) for _ in range(n)] for _ in range(n)]
check[7][0][0] = True
ans = False

while q:
    x, y, t = q.popleft()
    if x==0 and y==7:
        ans = True
    for i in range(9):
        nx, ny = x+dx[i], y+dy[i]
        nt = min(t+1, n)
        if 0<=nx<n and 0<=ny<n:
            if (nx-t>=0 and ground[nx-t][ny]=='#') or (nx-t-1>=0 and ground[nx-t-1][ny]=='#'):
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx, ny, nt))

print(1 if ans else 0)