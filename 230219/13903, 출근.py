def BFS():
    q = deque()
    for i in range(C):
        if block[0][i] == 1:
            q.append((0, i))
            ck[0][i] = 0
    while q:
        x, y = q.popleft()
        for i in range(N):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and block[nx][ny]==1 and ck[nx][ny]==-1:
                if nx == R-1:
                    return ck[x][y]+1
                ck[nx][ny] = ck[x][y]+1
                q.append((nx, ny))
    return -1

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())
block = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
N = int(sys.stdin.readline())
dx, dy = [0]*N, [0]*N
for i in range(N):
    dx[i], dy[i] = map(int, sys.stdin.readline().split())
ans = 10000
ck = [[-1]*C for _ in range(R)]
print(BFS())