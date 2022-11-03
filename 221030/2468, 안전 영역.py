import sys
from collections import deque
N = int(sys.stdin.readline())
graph = []
maxNum = 0
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]>value and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx, ny))

result = 0
for i in range(maxNum):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k]>i and visited[j][k]==0:
                bfs(j, k, i, visited)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)