def bfs():
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                d[i][j] = 0
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if a[nx][ny]!=1 and d[nx][ny]==-1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans==-1 or ans>cur:
        ans = cur

def go(index, cnt):
    if index == len(candi):
        if cnt == m:
            bfs()
    else:
        x, y = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 0
        go(index+1, cnt)

from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = -1
candi = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            a[i][j] = 0
            candi.append((i, j))
go(0, 0)
print(ans)