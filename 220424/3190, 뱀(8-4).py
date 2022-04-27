from collections import deque
import sys

def direction_change(d, c):
    if c == 'L':    # 뱀을 왼쪽으로
        d = (d-1) % 4
    else:    # 뱀을 오른쪽으로
        d = (d+1) % 4
    return d

N = int(sys.stdin.readline())    # 보드의 크기
K = int(sys.stdin.readline())    # 사과의 개수
board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())    # 방향 전환 횟수
times = {}
for i in range(L):    # 게임 시작 이후 방향을 바꿔야 하는 정보
    X, C = sys.stdin.readline().split()
    L = times[int(x)] = C

dy = [-1, 0, 1, 0]    # 위, 오른쪽, 아래, 왼쪽 순으로 탐색할 좌표
dx = [0, 1, 0, -1]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
board[y][x] = 2

while True:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:
        break
print(time)