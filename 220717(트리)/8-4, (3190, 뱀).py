from collections import deque
import sys

def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(sys.stdin.readline())
board = [[0]*N for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = 1

L = int(sys.stdin.readline())
Time = {}
for _ in range(L):
    X, C = sys.stdin.readline().split()
    Time[int(X)] = C

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
board[0][0] = 2

while True:
    y, x = y+dy[direction], x+dx[direction]
    if 0<=y<N and 0<=x<N and board[y][x] != 2:
        if board[y][x] != 1:
            dely, delx = snake.popleft()
            board[dely][delx] = 0
        snake.append([y, x])
        board[y][x] = 2
        if time in Time.keys():
            direction = change(direction, Time[time])
        time += 1
    else:
        break

print(time)