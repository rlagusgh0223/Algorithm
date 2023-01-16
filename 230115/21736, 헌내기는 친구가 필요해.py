def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if campus[nx][ny]=='O' and check[nx][ny]==0:
                check[nx][ny] = 1
                q.append((nx, ny))
            elif campus[nx][ny]=='P' and check[nx][ny]==0:
                check[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    if cnt > 0:
        return cnt
    else:
        return 'TT'

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
campus = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
check = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            print(bfs(i, j))