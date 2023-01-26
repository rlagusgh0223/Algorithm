from collections import deque
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
r, c = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
q.append((r, c))
board[r][c] = 2
ck = False
while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]
        if 0<=nr<5  and 0<=nc<5:
            if board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                q.append((nr, nc))
            elif board[nr][nc] == 1:
                print(board[r][c] - 1)  # -1, 0, 1과 구분하기 위해 시작점을 2로 주고 가는 부분마다 1을 더해줬으므로 도착지에서 2를 빼준다
                exit()
print(-1)