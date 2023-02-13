# pypy3로 돌려야 된다
def BFS(i, j):
    q = deque()
    q.append((i, j, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and A[nx][ny]!=1 and A[nx][ny]!=2:
                if A[nx][ny] != 0:
                    print("TAK")
                    return cnt + 1
                q.append((nx, ny, cnt+1))
                A[nx][ny] = 2
    return "NIE"

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if A[i][j] == 2:
            print(BFS(i, j))
            exit()