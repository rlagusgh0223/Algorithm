from collections import deque
import sys

def BFS():
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny][wall]==0:
                if Map[nx][ny]==0:
                    visit[nx][ny][wall] = visit[x][y][wall] + 1
                    q.append([nx, ny, wall])
                if wall == 0 and Map[nx][ny] == 1:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append([nx, ny, 1])
    return -1                    

N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
q = deque()
q.append([0, 0, 0])
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
print(BFS())