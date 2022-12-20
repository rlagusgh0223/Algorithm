def bfs(a, l, r):
    n = len(a)
    c = [[False]*n for _ in range(n)]
    ok = False
    for i in range(n):
        for j in range(n):
            if c[i][j] == False:
                c[i][j] = True
                q = deque()
                q.append((i, j))
                s = [(i, j)]
                total = a[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<n and 0<=ny<n and c[nx][ny]==False:
                            if l <= abs(a[nx][ny]-a[x][y]) <= r:
                                c[nx][ny] = True
                                q.append((nx, ny))
                                s.append((nx, ny))
                                total += a[nx][ny]
                                ok = True
                val = total//len(s)
                for x, y in s:
                    a[x][y] = val
    return ok

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    if bfs(a, L, R):
        ans += 1
    else:
        break
print(ans)