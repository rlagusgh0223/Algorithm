def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    check[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and war[nx][ny]==war[x][y] and check[nx][ny]==0:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))
                cnt += 1
    return cnt**2

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
war = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
check = [[0]*N for _ in range(M)]
w = b = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if war[i][j] == 'W' and check[i][j]==0:
            w += bfs(i, j)
        elif war[i][j] == 'B' and check[i][j]==0:
            b += bfs(i, j)
print(w, b)