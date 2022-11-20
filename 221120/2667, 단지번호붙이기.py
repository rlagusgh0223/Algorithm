def bfs(x, y):
    global ground
    q = deque()
    q.append((x, y))
    check[x][y] = cnt
    ans = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1 and check[nx][ny]==0:
                check[nx][ny] = cnt
                q.append((nx, ny))
                ans += 1
    ground.append(ans)


from collections import deque
import sys
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
check = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
ground = []
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and check[i][j]==0:
            cnt += 1
            bfs(i, j)
print(cnt)
ground.sort()
for now in ground:
    print(now)