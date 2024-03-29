# 백준 코드보다 이게 더 기억하기 쉬워서 이걸로 함
def BFS():
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, wall = q.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][wall]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny][wall]==0:
                if maze[nx][ny] == 0:
                    visit[nx][ny][wall] = visit[x][y][wall] + 1
                    q.append((nx, ny, wall))
                elif wall==0 and maze[nx][ny]==1:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append((nx, ny, 1))
    return -1    

from collections import deque
N, M = map(int, input().split())
maze = [[int(x) for x in input()] for _ in range(N)]
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(BFS())