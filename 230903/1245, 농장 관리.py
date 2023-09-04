from collections import deque
import sys

def BFS(x, y):
    global ck
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        check[x][y] = ck
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if mountain[nx][ny] > mountain[x][y]:
                    ck += 1
                    return False
                if check[nx][ny]<ck and mountain[nx][ny]==mountain[x][y]:
                    q.append((nx, ny))
    ck += 1
    return True

N, M = map(int, sys.stdin.readline().split())
mountain = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
cnt = 0
ck = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            if BFS(i, j):
                cnt += 1
print(cnt)