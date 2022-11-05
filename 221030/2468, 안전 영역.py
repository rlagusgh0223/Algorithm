def bfs(x, y, value, visit):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0 and lst[nx][ny]>value:
                q.append((nx, ny))
                visit[nx][ny] = 1

from collections import deque
import sys
N = int(sys.stdin.readline())
lst = []
maxNum = 0
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if maxNum < lst[i][j]:
            maxNum = lst[i][j]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0
for i in range(maxNum):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if lst[j][k] > i and visit[j][k]==0:
                bfs(j, k, i, visit)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)