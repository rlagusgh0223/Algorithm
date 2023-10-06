def BFS():
    q = deque()
    q.append((0, 0))
    check[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 방문을 열지 않고 지나갈수록 q의 앞에 입력하기 때문에
            # 처음 방문한 방은 가장 방문을 열지 않은 경우로 들어간다
            if 0<=nx<n and 0<=ny<n and check[nx][ny]==-1:
                if room[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    check[nx][ny] = check[x][y]
                else:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y]+1

from collections import deque
import sys
n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = [[-1]*n for _ in range(n)]
BFS()
print(check[n-1][n-1])