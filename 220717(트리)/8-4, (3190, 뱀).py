from collections import deque

def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
times = {}
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
board[y][x] = 2

while True:
    y, x = y+dy[direction], x+dx[direction]
    if 0<=y<N and 0<=x<N and board[y][x] != 2:
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