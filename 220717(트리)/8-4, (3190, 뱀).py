from collections import deque
import sys

def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]

k = int(sys.stdin.readline())
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

l = int(sys.stdin.readline())
times = {}
for _ in range(l):
    x, y = sys.stdin.readline().split()
    times[int(x)] = y

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
y, x = 0, 0
snake = deque([[y, x]])
board[y][x] = 2
time = 1

while True:
    y, x = y+dy[direction], x+dx[direction]
    if 0<=y<n and 0<=x<n and board[y][x] != 2:
        if board[y][x] != 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        snake.append([y, x])
        board[y][x] = 2
        if time in times.keys():
            direction = change(direction, times[time])
        time += 1
    else:
        break

print(time)