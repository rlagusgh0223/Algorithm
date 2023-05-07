# 미완성 코드
# 틀렸지만 테스트 케이스는 맞았다고 나온다
def BFS(tmin, attack):
    q = deque()
    q.append((tmin[1], tmin[2]))
    lst[tmin[1]][tmin[2]] += N+M
    check[tmin[1]][tmin[2]] = attack
    visit = [[[-1, -1]]*M for _ in range(N)]  # 최단거리를 기록하기 위한 배열
    visit[tmin[1]][tmin[2]] = [tmin[1], tmin[2]]
    bomb = [[True]*M for _ in range(N)]  # 이번 공격에 관계된 영역인지 확인
    bomb[tmin[1]][tmin[2]] = False
    # print("===visit===")
    # for i in range(N):
    #     print(*visit[i])
    # print("===check===")
    # for i in range(N):
    #     print(*check[i])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 가장자리에 가면 반대편으로 이동
            # 더해지는건 1씩이니까 칸이 많이 이동할 일은 없다
            if nx < 0:
                nx = N-1
            elif nx >= N:
                nx = 0
            if ny < 0:
                ny = M-1
            elif ny >= M:
                ny = 0

            # 최단거리 구하기
            if visit[nx][ny]==[-1, -1] and lst[nx][ny]!=0:
                visit[nx][ny] = [x, y]
                q.append((nx, ny))
            
            # 가장 강한 포탑을 만나면, 그리고 가는길이 끊어지지 않았다면(레이저)
            if lst[nx][ny] == tmax[0] and visit[nx][ny] != [-1, -1] and nx==tmax[1] and ny==tmax[2]:
                lst[nx][ny] -= tmin[0]
                bomb[nx][ny] = False
                bx, by = visit[nx][ny]
                while True:
                    if bx==tmin[1] and by==tmin[2]:
                        break
                    lst[bx][by] -= tmin[0]//2
                    bomb[bx][by] = False
                    if lst[bx][by] < 0:
                        lst[bx][by] = 0
                    bx, by = visit[bx][by]
                for bi in range(N):
                    for bj in range(M):
                        if lst[bi][bj] < 0:
                            lst[bi][bj] = 0
                        if bomb[bi][bj] and lst[bi][bj]!=0:
                            lst[bi][bj] += 1
                # print("===visit===")
                # for i in range(N):
                #     print(*visit[i])
                # print("===check===")
                # for i in range(N):
                #     print(*check[i])
                
                # for i in range(N):
                #     print(*bomb[i])
                return
            
            # 가장 강한 포탑을 만났지만 가는길이 끊어졌다면(폭탄)
            elif lst[nx][ny] == tmax[0] and visit[nx][ny] == [-1, -1]:
                print("vh")
                lst[nx][ny] -= tmin[0]
                bomb[nx][ny] = False
                for ci in range(-1, 2):
                    for cj in range(-1, 2):
                        if ci == cj == 0:
                            continue
                        CI, CJ = nx+ci, ny+cj
                        if CI < 0:
                            CI = N-1
                        elif CI >= N:
                            CI = 0
                        if CJ < 0:
                            CJ = M-1
                        elif CJ >= M:
                            CJ = 0
                        lst[CI][CJ] -= int(lst[nx][ny]/2)
                        bomb[CI][CJ] = False
                for ci in range(N):
                    for cj in range(M):
                        if lst[ci][cj] < 0:
                            lst[ci][cj] = 0
                        if bomb[ci][cj] and lst[ci][cj]!=0:
                            lst[ci][cj] += 1                        
                return



from collections import deque
import sys
N, M, K = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
tmax = [0, 0, 0]
tmin = [5001, 0, 0]
attack = 1  # check에 언제 공격했는지 입력하기 위한 변수
check = [[0]*M for _ in range(N)]  # 언제 공격했는지 확인하는 배열. 값이 클수록 최근

def search():
    global tmax, tmin, lst, check
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
                if check[x][y] > check[i][j]:
                    tmax = [lst[i][j], i, j]
                elif check[x][y] == check[i][j]:
                    if x+y > i+j:
                        tmax = [lst[i][j], i, j]
                    elif x+y == i+j:
                        if y > j:
                            tmax = [lst[i][j], i, j]

    for i in range(N):  # 배열 입력 및 가장 약한 포탑 / 가장 강한 포탑 확인
        for j in range(N):    
            # 최솟값(공격하는 포탑 구하기)
            # 기존의 최솟값보다 작은 값이 있다면 배열을 새로 만든다
            if lst[i][j]>0 and lst[i][j]<tmin[0]:
                tmin = [lst[i][j], i, j]
            # 기존의 최솟값과 같은 값이 있다면 차례대로 계산
            elif lst[i][j] == tmin[0]:
                x, y= tmin[1], tmin[2]
                if check[x][y] < check[i][j]:
                    tmin = [lst[i][j], i, j]
                elif check[x][y] == lst[i][j]:
                    if x+y < i+j:
                        tmin = [lst[i][j], i, j]
                    elif x+y == i+j:
                        if y < j:
                            tmin = [lst[i][j], i, j]

for i in range(K):
    search()
    tmin[0] += N+M
    BFS(tmin, i+1)
    print(tmax, tmin)
    for i in range(N):
        print(lst[i])
answer = 0
for i in range(N):
    answer = max(answer, max(lst[i]))
print(answer)