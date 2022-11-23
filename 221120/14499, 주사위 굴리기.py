import sys
N, M, x, y, K = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dice = [0] * 7
move = list(map(int, sys.stdin.readline().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in move:
    nx, ny = x+dx[i-1], y+dy[i-1]
    if 0<=nx<N and 0<=ny<M:
        if i == 1:
            temp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = temp
        elif i == 2:
            temp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = temp
        elif i == 3:
            temp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = temp
        else:
            temp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = temp
        x, y = nx, ny
        if a[x][y] == 0:
            a[x][y] = dice[6]
        else:
            dice[6] = a[x][y]
            a[x][y] = 0
        print(dice[1])