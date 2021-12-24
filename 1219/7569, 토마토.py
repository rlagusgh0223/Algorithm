from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]

for i in range(H):
    for j in range(N):
        graph[i][j] = list(map(int, sys.stdin.readline().split()))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append([i,j,k])
                visited[i][j][k] = 1
            elif graph[i][j][k] == -1:
                visited[i][j][k] = -1

while q:
    z, x, y = q.popleft()
    for i in range(H):
        for j in range(4):      # 지금 위치의 앞, 뒤, 좌, 우만 체크
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[i][nx][ny] == 0 and visited[i][nx][ny] == 0:
                    visited[i][nx][ny] = visited[i][x][y] + 1
                    q.append([i, nx, ny])


                for i in range(H):
                    for j in range(N):
                        for k in range(M):
                            print(visited[i][j][k], end='\t')
                        print()
                    print()
                print("===============================")
        
    for j in range(2):      # 지금 위치의 위, 아래만 체크
        nz = z + dz[j]
        if 0 <= nz < H:
            if graph[nz][x][y] == 0 and visited[nz][x][y] == 0:
                visited[nz][x][y] = visited[z][x][y] + 1
                q.append([nz, x, y])

ans = 0
endFlag = True
for i in range(H):
    for j in range(N):
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

if endFlag:
    print(ans-1)


# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             print(visited[i][j][k], end='\t')
#         print()
#     print()