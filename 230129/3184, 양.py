def BFS(i, j):
    q = deque()
    q.append((i, j))
    v, o = 0, 0
    if yard[i][j] == 'v':
        v += 1
    elif yard[i][j] == 'o':
        o += 1
    yard[i][j] = 'c'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and yard[nx][ny]!='#' and yard[nx][ny]!='c':
                if yard[nx][ny] == 'v':
                    v += 1
                elif yard[nx][ny] == 'o':
                    o += 1
                q.append((nx, ny))
                yard[nx][ny] = 'c'
    if v>=o:
        o = 0
    else:
        v = 0
    return v, o

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())
yard = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
W, S = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(R):
    for j in range(C):
        if yard[i][j]=='v' or yard[i][j]=='o':
            v, o = BFS(i, j)
            W, S = W+v, S+o
print(S, W)