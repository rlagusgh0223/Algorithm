#그냥 그래프에서 바로 더하는 방식으로 해도 될 것 같지만
#원본을 건드리는건 좋지 않을 것 같아서 visited에 표시하는걸로 했따
from collections import deque
import sys

dx = [-1, 1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def BFS(x, y):
    global graph
    cnt = 1
    q = deque()
    q.append([x, y])
    graph[x][y] = cnt
    print(graph)
    print(graph[x][y])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[nx][ny] == 1:
                    q.append([nx, ny])
                    graph[nx][ny] = cnt
                    cnt += 1
    for i in range(w):
        print(graph[i])
    print(cnt)

while True:
    h, w = map(int, sys.stdin.readline().split())
    land = 0
    if w == 0 and h == 0:
        break
    else:
        graph = [0] * w
        for i in range(w):
            graph[i] = list(map(int, sys.stdin.readline().split()))
        for i in range(w):
            for j in range(h):
                if graph[i][j] == 1:
                    BFS(i, j)
                    land += 1
        print(land)