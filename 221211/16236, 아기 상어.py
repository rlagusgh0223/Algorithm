def bfs(a, x, y, size):
    ans = []
    d = [[-1]*n for _ in range(n)]
    d[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and d[nx][ny]==-1:
                ok = False
                eat = False
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size:
                    ok = True
                    eat = True
                elif a[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]

from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if exp == size:
        exp = 0
        size += 1
    x, y = nx, ny
print(ans)