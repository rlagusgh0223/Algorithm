from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())   #가로, 세로줄 수 입력
graph = [0] * N                                 #가로줄(x)만큼 그래프 작성
for i in range(N):                              #세로줄(y)값 리스트로 작성
    graph[i] = list(map(int,sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]                              #주변을 탐색하기 위한 좌표
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]     #방문한적이 있는지 표시할 겸, 거리 측정을 위해 사용하는 리스트

def BFS(x, y):
    visited[x][y] = 1                           #시작점은 거리 1로 시작
    q = deque()                                 #큐 선언 및 시작점 입력
    q.append([x, y])
    while q:                                    #큐에 값이 있는한 반복
        now = q.popleft()                       #큐에 가장 먼저 입력한 값 출력
        x = now[0]                              #큐에서 나온 값(지금 x, y좌표) 입력
        y = now[1]
        for i in range(4):
            nx = x + dx[i]                      #다음 탐색할 x, y 좌표 입력
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:     #다음 좌표가 그래프 범위 안에 있다면
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:     #미로에서 갈 수 있는 곳이고 방문한 적이 없다면
                    q.append([nx, ny])          #다음 좌표 q에 입력
                    visited[nx][ny] = visited[x][y] + 1             #다음 좌표에는 현재 좌표의 거리 + 1

BFS(0,0)                                        #시작 위치는 정해졌으므로 바로 BFS에 입력

print(visited[N-1][M-1])                        #도착 위치에 거리 출력