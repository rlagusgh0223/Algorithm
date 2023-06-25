# https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description?page=3&pageSize=20
# 1 ~ n : 오른쪽
# n+1 ~ 2n : 위
# 2n+1 ~ 3n : 왼쪽
# 3n+1 ~ 4n : 아래
# 방향으로 공 던지는거 반복
# 해당 줄에 처음으로 만나는 사람의 점수**2만큼 점수 얻음
# 점수 획득 후 방향 바꿈
# 공을 한 번 던질 때 마다 한 칸씩 전진함

# 해야되는것
# 맨 처음에 일단 한 칸 전진하는 과정이 빠졌음
# 1. 머리/꼬리 사람 바꾸기
# 2. 앞으로 한 칸 전진

# 앞으로 한 칸 전진, visit로 다시 순서 붙이기
def go(x, y):
    for i in range(n):
        print(ground[i])
    print()
    q = deque()
    q.append((x, y, 1))
    ck = [[0]*n for _ in range(n)]
    while q:
        x, y, cnt = q.popleft()
        print(x, y, cnt)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            print(nx, ny)
            for i in range(n):
                print(ground[i])
            # 맨 처음 1이 4와 바뀔때
            if ground[nx][ny]==4 and ground[x][y]==1:  # 맨 처음 1일때
                visit[nx][ny] = cnt
                q.append((x, y, cnt+1))  # 1과 4를 바꿀거고 거기에서 점차적으로 나갈거니까 1이 있던 위치 입력
                ck[nx][ny] = 1
                ground[nx][ny], ground[x][y] = ground[x][y], ground[nx][ny]
            elif 2<=ground[nx][ny]<=3 and ck[nx][ny]==0 and cnt>1:  # 이후 옆에 있는 자리가 2 또는 3이고 방문한 적이 없으면
                q.append((nx, ny, cnt+1))
                ck[x][y] = 1
                visit[x][y] = cnt+1
                ground[nx][ny], ground[x][y] = ground[x][y], ground[nx][ny]
                if ground[nx][ny]==3:
                    ck[nx][ny] = 1

# 발견한 사람의 모임에서 1과 3 위치 파악
def turn(i, j):
    q = deque()
    q.append((i, j))
    ck = [[0]*n for _ in range(n)]
    ck[i][j] = 1
    human = []
    if ground[i][j]==1 or ground[i][j]==3:
        human.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and 1<=ground[nx][ny]<=3 and ck[nx][ny]==0:
                if ground[nx][ny]==1 or ground[nx][ny]==3:
                    human.append([nx, ny])
                    if len(human) == 2:
                        hx, hy, hnx, hny = human[0][0], human[0][1], human[1][0], human[1][1]
                        ground[hx][hy], ground[hnx][hny] = ground[hnx][hny], ground[hx][hy]
                        if ground[hx][hy] == 1:
                            go(hx, hy)
                        elif ground[hnx][hny] == 1:
                            go(hnx, hny)
                q.append((nx, ny))
                ck[nx][ny] = 1
    
    # print("visit")
    # for i in range(n):
    #     print(visit[i])


def BFS(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and 0<ground[nx][ny]<4 and visit[nx][ny]==0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

def Round(k):
    global ans
    for i in range(n):  # 오른쪽으로
        for j in range(n):
            if 0 < ground[i][j] < 4:
                ans += visit[i][j]**2
                turn(i, j)
                break
        k -= 1
        if k == 0:
            return k
    for i in range(n, 2*n):   # 위로
        for j in range(n-1, -1, -1):
            if 0 < ground[j][i-n] < 4:
                ans += visit[j][i-n]**2
                turn(i, j)
                break
        k -= 1
        if k == 0:
            return k
    I = 1
    for i in range(2*n, 3*n):  # 왼쪽으로
        for j in range(n-1, -1, -1):
            if 0 < ground[n-I][j] < 4:
                ans += visit[n-I][j]**2
                turn(i, j)
                break
        k -= 1
        if k == 0:
            return k
    I = n-1
    for i in range(3*n, 4*n):  # 아래로
        for j in range(n):
            if 0 < ground[j][I] < 4:
                ans += visit[j][I]**2
                turn(i, j)
                break
        k -= 1
        if k == 0:
            return k
        I -= 1


from collections import deque
import sys
n, m, k = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[0]*n for _ in range(n)]

# 사람별 점수를 주기 위해 BFS 사용
for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and ground[i][j]==1:
            BFS(i, j)

# 4면을 다 돌아도 k가 남았다면 k가 사라질때까지 반복
while k > 0:
    k = Round(k)
print(ans)
# for i in range(n):
#     print(ground[i])