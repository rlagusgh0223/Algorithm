# 모범답안이랑 똑같아 보이는데 틀렸단다
from collections import deque

def change(d, c):
    if c=='L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

N = int(input())
K = int(input())
Map = [[0]*N for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    Map[x-1][y-1] = 1

L = int(input())
Time = {}
for i in range(L):
    x, y = input().split()
    Time[int(x)] = y

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
Map[y][x] = 2

while True:
    y, x = y+dy[direction], x+dx[direction]
    if 0<=y<N and 0<=x<N and Map[y][x] != 2:
        if Map[y][x] != 1:
            delY, delX = snake.popleft()
            Map[delY][delX] = 0
        Map[y][x] = 2
        snake.append([y, x])
        if time in Time.keys():
            direction = change(direction, Time[time])
        time += 1
    else:
        break

print(time)