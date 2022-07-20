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
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())
Time = {}
for _ in range(L):
    x, c = sys.stdin.readline().split()
    Time[int(x)] = c

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
time = 1
Y, X = 0, 0
snake = deque([[Y, X]])
board[Y][X] = 2

while True:
    Y, X = Y+dy[direction], X+dx[direction]
    if 0<=Y<N and 0<=X<N and board[Y][X] != 2:
        if board[Y][X] != 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        snake.append([Y, X])
        board[Y][X] = 2
        if time in Time.keys():
            direction = change(direction, Time[time])
        time += 1
    else:
        break

print(time)