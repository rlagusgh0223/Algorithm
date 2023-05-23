# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/description?page=3&pageSize=20
# 반례
# 4 4 3
# 6 8 0 1
# 0 0 0 0
# 0 0 0 0
# 0 0 8 0
# 정답 : 12

# 10 10 20
# 995 3976 1850 0 0 0 0 0 2823 0
# 0 2197 4554 0 3991 0 0 0 0 0
# 2243 918 206 2051 0 0 0 0 0 2354
# 0 0 2211 394 3896 2763 0 0 3580 3094
# 0 0 4364 0 0 0 0 0 0 4990
# 0 0 0 0 0 0 736 0 1159 0
# 1374 0 2610 3165 3653 0 2651 0 0 0
# 4493 0 1423 0 2416 0 0 0 3580 0
# 0 4112 3779 0 3654 1247 0 0 132 712
# 92 2643 1459 4675 4838 0 2539 850 2040 2153

# 995   3976    1850    0       0       0       0       0   2823    0
# 0     2197    4554    0       3991    0       0       0   0       0
# 2243  918     206     2051    0       0       0       0   0       2354
# 0     0       2211    394     3896    2763    0       0   3580    3094
# 0     0       4364    0       0       0       0       0   0       4990
# 0     0       0       0       0       0       736     0   1159    0
# 1374  0       2610    3165    3653    0       2651    0   0       0
# 4493  0       1423    0       2416    0       0       0   3580    0
# 0     4112    3779    0       3654    1247    0       0   132     712
# 92    2643    1459    4675    4838    0       2539    850 2040    2153
# 답 : 4168

# 미완성 코드
# 6%까지는 맞았다고 나온다
def BFS(tmin, attack):
    q = deque()
    X, Y = tmin[1], tmin[2]
    q.append((X, Y))
    lst[X][Y] += N+M
    check[X][Y] = attack
    visit = [[[-1, -1]]*M for _ in range(N)]  # 최단거리를 기록하기 위한 배열
    visit[X][Y] = [X, Y]
    bomb = [[True]*M for _ in range(N)]  # 이번 공격에 관계된 영역인지 확인
    bomb[X][Y] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x+dx[i])%N, (y+dy[i])%M

            # 최단거리 구하기
            if visit[nx][ny]==[-1, -1] and lst[nx][ny]!=0:
                visit[nx][ny] = [x, y]
                q.append((nx, ny))
            
            # 가장 강한 포탑을 만나면, 그리고 가는길이 끊어지지 않았다면(레이저)
            if lst[nx][ny] == tmax[0] and visit[nx][ny] != [-1, -1] and nx==tmax[1] and ny==tmax[2]:
                print("레이저 공격")
                lst[nx][ny] -= tmin[0]
                bomb[nx][ny] = False
                bx, by = visit[nx][ny]
                while True:
                    if bx==tmin[1] and by==tmin[2]:
                        break
                    lst[bx][by] -= tmin[0]//2
                    bomb[bx][by] = False
                    # if lst[bx][by] < 0:
                    #     lst[bx][by] = 0
                    bx, by = visit[bx][by]
                for bi in range(N):
                    for bj in range(M):
                        if lst[bi][bj] < 0:  # 포탑이 음수가 되면 0으로 바꿔줌(음수 값은 없다)
                            lst[bi][bj] = 0
                        if bomb[bi][bj] and lst[bi][bj]!=0:  # 이번 공격과 관계 없는 곳이고 포탑이 존재한다면
                            lst[bi][bj] += 1  # 포탑의 생명력 1 증가
                return
            
    # 가장 강한 포탑을 만났지만 가는길이 끊어졌다면(폭탄)
    if visit[tmax[1]][tmax[2]]==[-1, -1]:
        nx, ny = tmax[1], tmax[2]
        print("폭탄 공격")
        lst[nx][ny] -= tmin[0]  # 폭탄 위치 값 감소
        bomb[nx][ny] = False
        # 폭탄 주변 8곳의 값 감소
        for ci in range(-1, 2):
            for cj in range(-1, 2):
                if ci == cj == 0:
                    continue
                CI, CJ = (nx+ci)%N, (ny+cj)%M
                if CI==tmin[1] and CJ==tmin[2]:
                    continue
                lst[CI][CJ] -= int(lst[X][Y]/2)
                bomb[CI][CJ] = False
        for ci in range(N):
            for cj in range(M):
                if lst[ci][cj] < 0:
                    lst[ci][cj] = 0
                if bomb[ci][cj] and lst[ci][cj]!=0:
                    lst[ci][cj] += 1                        
        return


def search():
    global tmax, tmin, lst, check  # 최댓값, 최솟값, 포탑리스트, 공격포탑 표시 리스트 수정 가능하다고 선언

    # 공격자 구하는 반복문
    for i in range(N):  # 배열 입력 및 가장 약한 포탑 / 가장 강한 포탑 확인
        for j in range(N):    
            if lst[i][j]==0:
                continue
            # 최솟값(공격하는 포탑 구하기)
            # 기존의 최솟값보다 작은 값이 있다면 배열을 새로 만든다
            if lst[i][j]<tmin[0]:
                tmin = [lst[i][j], i, j]
            # 기존의 최솟값과 같은 값이 있다면 차례대로 계산
            elif lst[i][j] == tmin[0]:
                x, y= tmin[1], tmin[2]
                if check[x][y] < check[i][j]:  # 이번 포탑이 더 최근에 공격했다면 공격포탑 수정
                    tmin = [lst[i][j], i, j]
                elif check[x][y] == lst[i][j]:
                    if x+y < i+j:  # 이번 포탑의 행+열의 합이 더 큰 경우 공격포탑 수정
                        tmin = [lst[i][j], i, j]
                    elif x+y == i+j:
                        if y < j:  # 이번 포탑의 열 값이 더 큰 경우 공격 포탑 수정
                            tmin = [lst[i][j], i, j]

    # 공격 당하는 포탑 구하는 반복문
    for i in range(N-1, -1, -1):  # 배열 입력 및 가장 약한 포탑 / 가장 강한 포탑 확인
        for j in range(N-1, -1, -1):
            # 만약 포탑이 없는곳이라면 통과
            if lst[i][j] == 0:
                continue
            # 최대값(공격 당하는 포탑) 구하기
            # 기존의 최댓값보다 큰 값이 있다면 배열을 아예 새로 만든다
            if lst[i][j] > tmax[0]:
                tmax = [lst[i][j], i, j]
            # 기존의 최댓값과 같은 값이 있다면 차례대로 계산
            elif lst[i][j] == tmax[0]:
                x, y = tmax[1], tmax[2]
                if check[x][y] > check[i][j]:  # 지금 포탑이 더 먼저 공격했다면
                    tmax = [lst[i][j], i, j]
                elif check[x][y] == check[i][j]:
                    if x+y > i+j:  # 행과 열의 합이 더 작다면
                        tmax = [lst[i][j], i, j]
                    elif x+y == i+j:
                        if y > j:  # 열 값이 더 작다면
                            tmax = [lst[i][j], i, j]
    if tmin[1]==tmax[1] and tmin[2]==tmax[2]:  # 포탑이 하나만 남은 경우에는 완전정지 한다
        exit()

from collections import deque
import sys
N, M, K = map(int, sys.stdin.readline().split())  # 맵의 세로, 가로, 공격의 반복 횟수
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
tmax = [0, 0, 0]  # max값, x좌표, y좌표
tmin = [5001, 0, 0]  # min값, x좌표, y좌표
attack = 1  # check에 언제 공격했는지 입력하기 위한 변수
check = [[0]*M for _ in range(N)]  # 언제 공격했는지 확인하는 배열. 값이 클수록 최근

for i in range(K):
    search()  # 가장 약한 포탑(공격자)와 가장 강한 포탑(공격을 당하는 포탑)을 찾는 함수
    tmin[0] += N+M
    BFS(tmin, i+1)
answer = 0
for i in range(N):
    answer = max(answer, max(lst[i]))
print(answer)