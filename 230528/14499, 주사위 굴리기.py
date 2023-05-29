import sys
N, M, x, y, K = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))
ans = []
dice = [[0], [0]*4, [0]]  # 왼쪽 벽면, 가운데라인, 오른쪽 벽면
# 4
# 2 1 5 6
# 3
# 위와 같이 입력된다면 주사위라고 생각하고 모양을 만들면 아래와 같은 모양으로 생각한다
# 4 2 3
#   1
#   5
#   6
for now in order:
    # 주사위 돌리기
    if now==1 and 0<=x<N and 0<=y+1<M:  # now는 방향, x, y는 주사위의 위치를 나타낸다
        y += 1  # 주사위를 동쪽으로 한 칸 이동
        dice[0][0], dice[1][2], dice[2][0], dice[1][0] = dice[1][0], dice[0][0], dice[1][2], dice[2][0]  # 주사위 값이 오른쪽에서 왼쪽으로 움직인다
        ans.append(dice[1][2])  # 주사위 천장의 값 출력 배열에 입력
    elif now==2 and 0<=x<N and 0<=y-1<M:
        y -= 1  # 주사위를 서쪽으로 한 칸 이동
        dice[0][0], dice[1][2], dice[2][0], dice[1][0] = dice[1][2], dice[2][0], dice[1][0], dice[0][0]  # 주사위 값이 왼쪽에서 오른쪽으로 움직인다
        ans.append(dice[1][2])
    elif now==3 and 0<=x-1<N and 0<=y<M:
        x -= 1  # 주사위를 북쪽으로 한 칸 이동
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][1], dice[1][2], dice[1][3], dice[1][0]  # 주사위 값이 아래에서 위로 올라간다
        ans.append(dice[1][2])
    elif now==4 and 0<=x+1<N and 0<=y<M:
        x += 1  # 주사위를 남쪽으로 한 칸 이동
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][3], dice[1][0], dice[1][1], dice[1][2]  # 주사위 값이 위에서 아래로 내려간다
        ans.append(dice[1][2])
    else:
        continue

    # 주사위에 값 넣기
    if ground[x][y] == 0:  # 바닥의 값이 0이면 주사위의 바닥면 값 복사
        ground[x][y] = dice[1][0]
    else:  # 바닥의 값이 0이 아니면 바닥과 주사위의 바다면 값 교환
        dice[1][0], ground[x][y] = ground[x][y], 0

for now in ans:
    print(now)