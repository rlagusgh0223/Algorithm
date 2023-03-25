import sys
# 가로, 세로
C, R = map(int, sys.stdin.readline().split())
seat = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir, x, y = 0, 0, R-1
lst = [[0]*C for _ in range(R)]
if seat > R*C:
    print(0)
    exit()
for now in range(1, R*C+1):
    lst[y][x] = now
    if now == seat:
        print(x+1, R-y)
        exit()
    x += dx[dir]
    y += dy[dir]
    if x<0 or y<0 or x>=C or y>=R or lst[y][x]!=0:
        x -= dx[dir]
        y -= dy[dir]
        dir = (dir+1) % 4
        x += dx[dir]
        y += dy[dir]