# 불이지나간 다음 사람이 지나가면 한 사이클이 되어 따로 계산해주지 않아도 불이 지나간 곳은 사람이 지나갈 수 없게 된다
def BFS():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if build[x][y]=='@' and (nx<0 or nx>=h or ny<0 or ny>=w):
                return visit[x][y]+1
            elif 0<=nx<h and 0<=ny<w and visit[nx][ny]==-1:
                if build[x][y]=='*' and (build[nx][ny]=='.' or build[nx][ny]=='@'):
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    build[nx][ny] = '*'
                elif build[x][y]=='@' and build[nx][ny]=='.':
                    visit[nx][ny] = visit[x][y] + 1
                    build[nx][ny] = '@'
                    q.append((nx, ny))
    return "IMPOSSIBLE"

from collections import deque
import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(sys.stdin.readline())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    q = deque()
    visit = [[-1]*w for _ in range(h)]
    build = []
    for i in range(h):
        build.append(list(sys.stdin.readline().rstrip()))
        for j in range(w):
            if build[i][j] == '@':
                start = (i, j)
                visit[i][j] = 0
            elif build[i][j] == '*':
                q.append((i, j))
                visit[i][j] = 0
    q.append(start)
    print(BFS())