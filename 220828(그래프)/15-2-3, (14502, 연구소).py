from collections import deque

def BFS(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and temp[x][y]==0:
                temp[i][j] = 2

def get_score():
    global answer
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    answer = max(score, answer)

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
        return
    for i in range(x, N):
        if i == x:
            for j in range(y+1, M):
                if Map[i][j] == 0:
                    Map[i][j] = 1
                    DFS(depth+1, x, y)
                    Map[i][j] = 0
        else:
            for j in range(M):
                if Map[i][j] == 0:
                    Map[i][j] = 1
                    DFS(depth+1, x, y)
                    Map[i][j] = 0

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
temp = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
DFS(0, 0, -1)
print(answer)