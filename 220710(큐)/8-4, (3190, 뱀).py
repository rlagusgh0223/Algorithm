from collections import deque

def change(d, c):
    if c == 'L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(input())
K = int(input())
Map = [[0]*N for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    Map[a-1][b-1] = 1
L = int(input())
times = {}
for i in range(L):
    x, y = input().split()
    times[int(x)] = y

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
Map[y][x] = 2

while True:
    y, x = y+dy[direction], x+dx[direction]
    if 0<=x<N and 0<=y<N and Map[y][x]!=2:
        if Map[y][x] != 1:
            delY, delX = snake.popleft()
            Map[delY][delX] = 0
        Map[y][x] = 2
        snake.append([y,x])
        if time in times.keys():
            direction = change(direction, times[time])
        time += 1
    else:
        break

print(time)