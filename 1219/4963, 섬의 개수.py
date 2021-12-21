from collections import deque
import sys

dx = [-1, 1, 0, 0, 1, -1, -1, 1]                # 대각선까지 검사해야 하니까
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def BFS(x, y):
    global graph                                # 그래프를 아래 while문에서 선언했으니까 여기서 수정하려면 global써야한다
    cnt = 2                                     # 문제에서 요청하지는 않았지만 섬의 면적도 물어본다고 가정하여 작성(이거 안쓸거면 visited 써야 된다)
                                                # cnt를 1로 주면 개수 1과 섬의 면적을 말하는 1이 겹치므로 섬의 면적을 셀 때 오차가 발생한다
    q = deque()
    q.append([x, y])
    graph[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[nx][ny] == 1:
                    q.append([nx, ny])
                    cnt += 1
                    graph[nx][ny] = cnt
    #print(cnt-1)

while True:                                             # 0 0을 입력할때까지 반복
    h, w = map(int, sys.stdin.readline().split())       # 여기서는 세로, 가로를 입력하므로 x, y랑은 크로스로 입력
    land = 0                                            # 섬 수 계산할 변수
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
                    land += 1                           # BFS가 한번 돈다는건 땅이 인접한 경우를 나왔다는 뜻이므로 graph에 표시 끝내고 섬의 수 증가
        print(land)