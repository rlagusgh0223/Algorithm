def BFS(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0:
                if iceberg[nx][ny]>0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                # 지금 위치가 빙산이고, 주변이 0이라면 빙산에서 1 빼기(빙산이었던 곳은 visit의 값이 1이기 때문에 계산 안된다)
                if iceberg[x][y]>0 and iceberg[nx][ny]==0:
                    iceberg[x][y] -= 1
                    if iceberg[x][y] < 0:
                        iceberg[x][y] = 0

from collections import deque
import sys
ans = 0
N, M = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while True:
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    ck = True
    # 빙산이 2덩이 이상인지 확인
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]>0 and visit[i][j]==0:
                BFS(i, j)
                ck = False
                cnt += 1
                if cnt >= 2:
                    print(ans)
                    exit()
    # 빙산이 다 녹아도 두 덩어리 이상으로 분리되지 않은 경우
    if ck:
        print(0)
        exit()
    ans += 1