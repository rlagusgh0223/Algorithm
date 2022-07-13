from collections import deque
import sys

def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0]*N for _ in range(N)]

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1
L = int(sys.stdin.readline())
times = {}
for i in range(L):
    x, y = sys.stdin.readline().split()
    times[int(x)] = y

direction = 1
x, y = 0, 0
snake = deque([[y, x]])
time = 1
board[0][0]=2

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    x, y = x+dx[direction], y+dy[direction]
    if 0<=x<N and 0<=y<N and board[y][x]!=2:
        if board[y][x] != 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
    
        if time in times.keys():
            direction = change(direction, times[time])
        time += 1
    else:
        break

print(time)