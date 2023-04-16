def BFS(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and temp[nx][ny]==0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def get_score():
    global answer
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

def DFS(depth, x, y):
    if depth == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = Map[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    BFS(i, j)
        get_score()
    else:
        for i in range(x, N):
            if i == x:
                for j in range(y, M):
                    if Map[i][j] == 0:
                        Map[i][j] = 1
                        DFS(depth+1, i, j+1)
                        Map[i][j] = 0
            else:
                for j in range(M):
                    if Map[i][j] == 0:
                        Map[i][j] = 1
                        DFS(depth+1, i, j+1)
                        Map[i][j] = 0

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
temp = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
DFS(0, 0, 0)
print(answer)