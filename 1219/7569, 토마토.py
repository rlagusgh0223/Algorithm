#pypy3로 하면 답 나온다
from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(H):                          # 토마토 입력
    for j in range(N):
        graph[i][j] = list(map(int, sys.stdin.readline().split()))
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append([i,j,k])
                visited[i][j][k] = 1
            elif graph[i][j][k] == -1:
                visited[i][j][k] = -1

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                q.append([nz, nx, ny])

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