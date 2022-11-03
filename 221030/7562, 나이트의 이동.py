from collections import deque
import sys

def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    visit[a][b] = 1
    while q:
        x, y = q.popleft()
        if x==c and y==d:
            print(visit[x][y] - 1)
            return True
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and visit[nx][ny]==0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    return False

n = int(sys.stdin.readline())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
for i in range(n):
    l = int(sys.stdin.readline())
    visit = [[0]*l for _ in range(l)]
    x, y = map(int, sys.stdin.readline().split())
    nx, ny = map(int, sys.stdin.readline().split())
    bfs(x, y, nx, ny)