def bfs(x, y, rain, visit):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and ground[nx][ny]>rain and visit[nx][ny]==0:
                visit[nx][ny] = 1
                q.append((nx, ny))

from collections import deque
import sys
N = int(sys.stdin.readline())
ground = []
maxNum = 0
for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if maxNum < ground[i][j]:
            maxNum = ground[i][j]
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for rain in range(maxNum):  # 내리는 비의 양(비의 높이에 따라 잠기는 지역을 계산하기 위해). 0부터 시작하지 않으면 에러난다. 왜? 어차피 2 미만은 다 영역이 1로 나오는거 아닌가?
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if ground[i][j]>rain and visit[i][j]==0:
                bfs(i, j, rain, visit)
                cnt += 1  # 인접한 곳은 같은 영역으로 bfs를 이용해 구하며, 새로 bfs를 동작한다는 뜻은 새로운 영역이라는 것이다
    if result < cnt:
        result = cnt
print(result)