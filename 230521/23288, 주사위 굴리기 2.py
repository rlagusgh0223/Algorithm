from collections import deque
import sys
# 동쪽부터 시계방향으로 돌아가는 좌표
dir = ans = x = y = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [int(x) for x in range(7)]  # 어차피 내가 위치 바꾸는 거니까 편의를 위해 0~6까지 배열을 만들었다. 사용하는건 1~6
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
    
    # A>B인 경우 이동 방향을 90도 시계 방향으로 회전
    if dice[6] > ground[x][y]:
        dir = (dir+1)%4
    # A<B인 경우 이동 방향을 90도 반시계 방향으로 회전
    elif dice[6] < ground[x][y]:
        dir = (dir-1)%4

    q.append((x, y))
    cnt = 1
    visit = [[0]*M for _ in range(N)]
    visit[x][y] = 1
    while q:
        X, Y = q.popleft()
        for i in range(4):
            nx, ny = X+dx[i], Y+dy[i]
            if 0<=nx<N and 0<=ny<M and ground[x][y]==ground[nx][ny] and visit[nx][ny]==0:
                visit[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    ans += cnt*ground[x][y]
print(ans)