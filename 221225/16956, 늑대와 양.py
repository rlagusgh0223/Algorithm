R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ck = False
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if nx<0 or nx>=R or ny<0 or ny>=C:
                    continue
                if M[nx][ny] == 'S':
                    ck = True
if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j]=='.':  # S 주변에만 울타리를 골라 치는것보다 그냥 전체적으로 울타리를 치는게 더 빠르다
                M[i][j]='D'
    for now in M:
        print(*now, sep='')