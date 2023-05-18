def BFS():
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 현재 지훈이인데 미로를 벗어나면 종료한다
            if maze[x][y]=='J' and (nx<0 or nx>=R or ny<0 or ny>=C):
                return cnt+1
            # 현재 지훈이인데 다음 공간이 지나갈 수 있는 공간이면 시간을 1 더하고 지나간다
            if maze[x][y]=='J' and maze[nx][ny]=='.':
                q.append((nx, ny, cnt+1))
                maze[nx][ny] = 'J'
            # 현재 불인데 미로 안이고 다음 공간이 지나갈 수 있는 공간이거나 지훈이가 다녀간 곳이면 지나간다
            elif 0<=nx<R and 0<=ny<C and maze[x][y]=='F' and (maze[nx][ny]== 'J' or maze[nx][ny]=='.'):
                q.append((nx, ny, cnt))
                maze[nx][ny] = 'F'
    # while을 벗어났다는건 지훈이가 미로 밖으로 나가지 못했다는 의미이므로 IMPOSSIBLE을 출력한다
    return "IMPOSSIBLE"

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
start = []  # 불이 하나뿐이라는 말이 없었으므로 여러곳에서 시작할 수 있다. 이러한 위치를 저장하기 위한 리스트
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            start.append((i, j, 0))
        elif maze[i][j] == 'J':
            q.append((i, j, 0))
# 예제를 보면 지훈이가 먼저 움직이고 불이 움직이는걸 알 수 있다
# 큐에 지훈이의 위치를 먼저 넣고 불의 위치를 나중에 넣어 지훈이가 먼저 움직이게 한다
for s in start:
    q.append(s)
print(BFS())