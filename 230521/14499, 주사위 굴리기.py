import sys
N, M, x, y, K = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))
ans = []
dice = [[0], [0]*4, [0]]  # 왼쪽 벽면, 가운데라인, 오른쪽 벽면
for now in order:
    # 주사위 돌리기
    if now==1 and 0<=x<N and 0<=y+1<M:
        y += 1
        dice[0][0], dice[1][2], dice[2][0], dice[1][0] = dice[1][0], dice[0][0], dice[1][2], dice[2][0]
        ans.append(dice[1][2])
    elif now==2 and 0<=x<N and 0<=y-1<M:
        y -= 1
        dice[0][0], dice[1][2], dice[2][0], dice[1][0] = dice[1][2], dice[2][0], dice[1][0], dice[0][0]
        ans.append(dice[1][2])
    elif now==3 and 0<=x-1<N and 0<=y<M:
        x -= 1
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][1], dice[1][2], dice[1][3], dice[1][0]
        ans.append(dice[1][2])
    elif now==4 and 0<=x+1<N and 0<=y<M:
        x += 1
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][3], dice[1][0], dice[1][1], dice[1][2]
        ans.append(dice[1][2])
    else:
        continue

    # 주사위에 값 넣기
    if ground[x][y] == 0:
        ground[x][y] = dice[1][0]
    else:
        dice[1][0], ground[x][y] = ground[x][y], 0

for now in ans:
    print(now)