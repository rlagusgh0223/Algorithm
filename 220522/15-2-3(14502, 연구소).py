from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
temp = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ans = 0

def BFS(x, y):    # 바이러스의 좌표를 받았을때 주변 빈칸으로 바이러스 전파
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and temp[nx][ny]==0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def get_score():    # 벽을 세운 후 빈 칸의 개수 구하는 함수
    global ans
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    ans = max(ans, score)

def DFS(depth, x, y):    # 깊이우선탐색을 이용해 벽을 세워보는 함수
    if depth == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    BFS(i, j)
        get_score()
        return
    for i in range(x, N):
        if i == x:
            for j in range(y+1, M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    DFS(depth+1, i, j)
                    graph[i][j] = 0
        else:
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    DFS(depth+1, i, j)
                    graph[i][j] = 0

DFS(0, 0, -1)
print(ans)