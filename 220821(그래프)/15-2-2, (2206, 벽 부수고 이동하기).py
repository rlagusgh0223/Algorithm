from collections import deque

def BFS(x, y, wall):
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1
    q = deque()
    q.append([x, y, wall])
    while q:
        x, y, wall = q.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][wall]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny][wall]==0:
                if maze[nx][ny]==0:
                    visit[nx][ny][wall] = visit[x][y][wall]+1
                    q.append([nx, ny, wall])
                if wall==0 and maze[nx][ny]==1:
                    visit[nx][ny][1] = visit[x][y][0]+1
                    q.append([nx, ny, 1])
    return -1                    

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(BFS(0, 0, 0))