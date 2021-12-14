from collections import deque
import sys
N = int(sys.stdin.readline())   #정사각형 모양의 범위 입력
ground = [0] * N                #땅을 입력받을 리스트 입력
visited = [[0 for _ in range(N)] for _ in range(N)]    #섬에 방문한적 있는지 체크할 리스트
dx = [0, 0, -1, 1]              #위, 아래, 앞, 뒤를 점검하기 위한 리스트
dy = [-1, 1, 0, 0]
cnt = 0                         #섬의 갯수 계산할 변수
graph = []                      #오름차순으로 섬을 정렬하기 위한 리스트

for i in range(N):              #섬의 정보 입력
    ground[i] = list(map(int, sys.stdin.readline().rstrip()))

def BFS(x, y, cnt):             #BFS에 시작점, cnt 전달
    q = deque()                 #BFS수행을 위해 큐 선언하고 시작점 입력
    q.append([x,y])
    visited[x][y] = cnt         #시작점 위치는 방문한 것이므로 현재 섬의 번호를 표시
    cal = 1                     #섬의 면적 계산할 변수 선언
    while q:                    #큐가 있는한 반복
        now = q.popleft()       #큐의 값 출력(좌표)
        x = now[0]              #출력된 좌표의 x, y 입력
        y = now[1]              #처음에는 BFS로 받은 x,y와 같으나 while문이 돌아가는동안 바뀌는걸 반영하기 위함
        for i in range(4):      #위, 아래, 앞, 뒤를 확인하기 위한 반복문
            nx = x + dx[i]      #다음 좌표는 현재 좌표에서 위, 아래, 앞, 뒤
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:                         #다음 좌표가 ground 안에 있다면
                if ground[nx][ny] == 1 and visited[nx][ny] == 0:    #그리고 방문한적이 없는 인접한 땅이라면
                    visited[nx][ny] = cnt                           #해당 땅 방문했다고 표시 후
                    q.append([nx, ny])                              #큐에 해당 땅의 좌표 입력
                    cal += 1                                        #해당 땅도 섬의 면적에 포함
    return cal                  #계산한 땅의 넓이 보내주어 리스트에 넣을 수 있도록 해줌

for i in range(N):              #정사각형의 그라운드 만큼 반복
    for j in range(N):
        if ground[i][j] == 1 and visited[i][j] == 0:                #섬은 있는데 방문한 적이 없을 경우
            cnt += 1            #섬의 갯수 증가
            now = BFS(i, j, cnt)
            graph.append(now)   #BFS종료 후 섬의 면적 graph에 입력

graph.sort()                    #오름차순 정렬
print(cnt)
for i in graph:                 #섬의 갯수, 각 섬의 면적 출력
    print(i)
