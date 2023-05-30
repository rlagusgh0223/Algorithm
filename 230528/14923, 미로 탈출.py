def BFS(x, y, check):
    q = deque()
    q.append((x, y, check))
    visit[check][x][y] = 1
    while q:
        x, y, check = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visit[check][nx][ny]==0:
                if nx==Ex-1 and ny==Ey-1:
                    return visit[check][x][y]
                elif maze[nx][ny] == 0:
                    visit[check][nx][ny] = visit[check][x][y] + 1
                    q.append((nx, ny, check))
                elif maze[nx][ny]==1 and check==0:
                    visit[1][nx][ny] = visit[0][x][y] + 1
                    q.append((nx, ny, 1))
    return -1

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[[0]*M for _ in range(N)] for _ in range(2)]
print(BFS(Hx-1, Hy-1, 0))