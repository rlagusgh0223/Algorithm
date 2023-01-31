def bfs(i, j):
    q = deque()
    q.append((i, j))
    lst[i][j] = -1
    ck = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and lst[nx][ny]==1:
                lst[nx][ny] = -1
                q.append((nx, ny))
                ck += 1
    return ck

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:      
            ans += 1
            cnt = max(cnt, bfs(i, j))
print(ans)
print(cnt)