def BFS(i, j):
    q = deque()
    q.append((i, j))
    v, k = 0, 0
    if ground[i][j] == 'v':
        v += 1
    else:
        k += 1
    ground[i][j] = '*'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and ground[nx][ny]!='#' and ground[nx][ny]!='*':
                if ground[nx][ny] == 'v':
                    v += 1
                elif ground[nx][ny] == 'k':
                    k += 1
                ground[nx][ny] = '*'
                q.append((nx, ny))
    if v < k:
        return 0, k
    else:
        return v, 0

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())
ground = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
V, K = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(R):
    for j in range(C):
        if ground[i][j]=='v' or ground[i][j]=='k':
            x, y = BFS(i, j)
            V += x
            K += y
print(K, V)