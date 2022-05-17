# 책의 모범답안 이지만 기존에 했던 풀이와 코드적으로 크게 다른 부분은 없는 것 같다
# 코드 길이는 좀 짧지만 시간은 같은것 같으니 그냥 원래 하던 풀이대로 하겠다

# BFS는 대략 아래의 형태를 따라간다
# bfs(x,y):
#   q = deque()
#   q.append((x,y))
#   while q:
#     x, y = q.popleft()
#     for i in range(len(dx))):
#       nx = x + dx[i]    # dx, dy는 인접 좌표를 나타내는 배열
#       ny = y + dy[i]    # 상, 하 , 좌, 우 가 될 수 도 있고 8방이 될 수 도 있어서 여기서는 len(dx)로 했다
#       if 0<=nx<N and 0<=ny<M and 방문한적이 없는지:
#         q.append(nx, ny)
#         [nx][ny] 좌표의 배열에 뭔가 변화

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()    # 큐 생성
q.append((0, 0))
def bfs():
    while q:    # 큐가 비어있지 않다면 반복
        x, y = q.popleft()    # 큐에 가장 먼저 삽입된 x, y 위치를 꺼낸다
        for k in range(len(d)):    # x, y에서 상하좌우로 이동한 위치 dx, dy
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < N and 0 <= dy < M:    # 다음으로 이동해야되는 dx, dy의 범위가 미로 안이고
                if maze[dx][dy] == 1:    # 아직 방문하지 않은 칸이라면
                    maze[dx][dy] = maze[x][y] + 1    # 다음으로 방문할 칸의 값을 현재 값 + 1로 바꿔준다
                    q.append((dx, dy))    # 큐에 다음 좌표를 넣는다

maze[0][0] = 1
bfs()
print(maze[N-1][M-1])