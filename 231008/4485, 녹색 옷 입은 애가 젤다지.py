def dijkstra():
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if x==N-1 and y==N-1:
            print(f"Problem {cnt}: {distance[x][y]}")
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                ncost = cost + cave[nx][ny]
                if ncost < distance[nx][ny]:
                    distance[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx, ny))

import sys, heapq
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    cnt += 1
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]
    dijkstra()