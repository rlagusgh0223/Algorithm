def BFS(x, y):
    q = deque()
    q.append((x, y))
    ground[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and ground[nx][ny]==-1:
                q.append((nx, ny))
                ground[nx][ny] = cnt

from collections import deque
T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(T):
    N, M, K = map(int, input().split())
    ground = [[0]*N for _ in range(M)]
    for i in range(K):
        y, x = map(int, input().split())
        ground[x][y] = -1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if ground[i][j]==-1:
                cnt += 1
                BFS(i, j)
    print(cnt)