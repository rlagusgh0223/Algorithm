from collections import deque
import sys
N, M ,K = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visit = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1
q = deque()
q.append((0, 0, 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y, wall = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if maze[nx][ny]==0 and visit[nx][ny][wall]==0:
            visit[nx][ny][wall] = visit[x][y][wall] + 1
            q.append((nx, ny, wall))
        elif maze[nx][ny]==1 and wall<K and visit[nx][ny][wall+1]==0:
            visit[nx][ny][wall+1] = visit[x][y][wall] + 1
            q.append((nx, ny, wall+1))
ans = -1
for i in range(K+1):
    if visit[N-1][M-1][i] == 0:
        continue
    if ans==-1 or ans>visit[N-1][M-1][i]:
        ans = visit[N-1][M-1][i]
print(ans)