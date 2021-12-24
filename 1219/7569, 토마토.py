from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]        #상자 위, 아래로 옮기기 위해(상자 높이가 얼마나 되든 인접한것부터 전파된다)

for i in range(H):                          # 토마토 입력
    for j in range(N):
        graph[i][j] = list(map(int, sys.stdin.readline().split()))

for i in range(H):                          # 최초의 토마토 위치 체크(-1도 체크해야 나중에 0으로 보지 않음)
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append([i,j,k])
                visited[i][j][k] = 1
            elif graph[i][j][k] == -1:
                visited[i][j][k] = -1

while q:
    z, x, y = q.popleft()
        
    for j in range(2):                      # 지금 높이의 위, 아래만 체크
        nz = z + dz[j]
        if 0 <= nz < H:
            if graph[nz][x][y] == 0 and visited[nz][x][y] == 0:
                visited[nz][x][y] = visited[z][x][y] + 1
                q.append([nz, x, y])

    for i in range(H):
        for j in range(4):                  # 지금 높이의 앞, 뒤, 좌, 우만 체크
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[i][nx][ny] == 0 and visited[i][nx][ny] == 0:
                    visited[i][nx][ny] = visited[i][x][y] + 1
                    q.append([i, nx, ny])

ans = 0
endFlag = True

for i in range(H):                  # 0이 있는지 확인
    for j in range(N):              # 하나라도 0이 있으면 -1 출력하고 종료
        for k in range(M):
            ans = max(ans, visited[i][j][k])
            if visited[i][j][k] == 0:
                print('-1')
                endFlag = False
                break
        if not endFlag:
            break
    if not endFlag:
        break

if endFlag:                         # 0이 없으면 ans-1. ans는 그래프의 값 중 최대값으로 이미 모든게 익었으면 1이 되니까 0, 나머지는 -1일로 한다
    print(ans-1)                    # -1을 하는 이유는 처음 시작을 0으로 하면 익지 않은것으로 판별하기 때문에 1로 시작하도록 코딩해서 그렇다