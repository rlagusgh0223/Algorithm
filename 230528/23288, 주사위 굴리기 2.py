from collections import deque
import sys
dir = ans = x = y = 0
# 동쪽부터 시계방향으로 돌아가는 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [int(x) for x in range(7)]  # 어차피 내가 위치 바꾸는 거니까 편의를 위해 0~6까지 배열을 만들었다. 사용하는건 1~6
# 1 ~ 6 위치 값은 아래와 같다(1이 천장이다)
#   2
# 4 1 3
#   5
#   6
N, M, K = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
for _ in range(K):
    xd, yd = x+dx[dir], y+dy[dir]
    # 만약 판을 벗어난다면 이동 방향을 반대로 한 다음 한 칸 굴러간다
    if xd<0 or xd>=N or yd<0 or yd>=M:
        dir = (dir+2)%4
    x, y = x+dx[dir], y+dy[dir]
    
    # 어느 방향으로 굴러가는지
    if dir == 0:  # 동쪽
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif dir == 1: # 남쪽
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
    elif dir == 2: # 서쪽
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif dir == 3: # 북쪽
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    
    # 주사위 바닥면의 값 > 칸에 있는 값 인 경우 이동 방향을 90도 시계 방향으로 회전(배열 순서)
    if dice[6] > ground[x][y]:
        dir = (dir+1)%4
    # 주사위 바닥면의 값 < 칸에 있는 값 인 경우 이동 방향을 90도 반시계 방향으로 회전(배열 역순)
    elif dice[6] < ground[x][y]:
        dir = (dir-1)%4

    # 이동한 부분과 같은 값의 면적을 계산
    q.append((x, y))
    cnt = 1
    visit = [[0]*M for _ in range(N)]  # 점검했는지 확인하는 배열
    visit[x][y] = 1
    while q:
        X, Y = q.popleft()
        for i in range(4):
            nx, ny = X+dx[i], Y+dy[i]
            # 다음 좌표가 지도 안에 있고 이전과 현재의 지도 위의 정수가 같으며 방문한 적이 없다면
            if 0<=nx<N and 0<=ny<M and ground[x][y]==ground[nx][ny] and visit[nx][ny]==0:
                visit[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    # 출력값에 현재 칸의 범위*지도의 정수 값을 더해준다
    ans += cnt*ground[x][y]
print(ans)