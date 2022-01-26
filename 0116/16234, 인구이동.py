from collections import deque
from struct import pack
import sys

N, L, R = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

flag = True
ans = -1
united = 0  # 연합한 국가인지 분간하고 연합이 여러개일 경우 구분하기 위한 변수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def open(x, y):     # 인구이동이 가능한 구간인지 확인
    global flag
    global visited
    visited[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == 0:
                flag = True
                return True
    return False

def BFS(x,y):
    global visited
    sum = graph[x][y]
    cnt = 1
    q = deque()
    q.append([x,y])
    unitedq = deque()
    unitedq.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if  L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    sum += graph[nx][ny]
                    cnt += 1
                    unitedq.append((nx,ny))
    while unitedq:
        r,c = unitedq.popleft()
        graph[r][c] = sum//cnt

while flag:
    flag = False
    ans += 1
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):          # 인구이동이 가능한 구간인지 확인하여 visited에 표시
        for j in range(N):
            if visited[i][j]==0 and open(i,j):
                BFS(i, j)

print(ans)