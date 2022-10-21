from collections import deque
import sys
M, N = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
check = [[-1]*M for _ in range(N)]
q = deque()
next_q = deque()
q.append((0, 0))
check[0][0] = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and check[nx][ny]==-1:
            if miro[nx][ny]==0:
                check[nx][ny] = check[x][y]
                q.append((nx, ny))
            else:
                check[nx][ny] = check[x][y]+1
                next_q.append((nx, ny))
    if not q:
        q = next_q
        next_q = deque()
print(check[N-1][M-1])