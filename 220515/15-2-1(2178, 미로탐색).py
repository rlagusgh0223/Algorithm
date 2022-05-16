from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()    # 큐 생성
q.append((0, 0))
def bfs():
    while q:    # 큐가 비어있지 않다면 반복
        x, y = q.popleft()    # 큐에 가장 먼저 삽입된 x, y 위치를 꺼낸다
        for k in range(len(d)):    # x, y에서 상하좌우로 이동한 위치 dx, dy
            dx = x + dx[k][0]
            dy = y + dy[k][0]
            if 0 <= dx < N and 0 <= dy < M:    # 다음으로 이동해야되는 dx, dy의 범위가 미로 안이고
                if maze[dx][dy] == 1:    # 아직 방문하지 않은 칸이라면
                    maze[dx][dy] = maze[x][y] + 1    # 다음으로 방문할 칸의 값을 현재 값 + 1로 바꿔준다
                    q.append((dx, dy))    # 큐에 다음 좌표를 넣는다

maze[0][0] = 1
bfs()
print(maze[N-1][M-1])