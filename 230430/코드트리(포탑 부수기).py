# 미완성 코드
def BFS(tmin):
    global attack
    q = deque()
    q.append((tmin[1], tmin[2]))
    attack += 1
    check[tmin[1]][tmin[2]] = attack
    visit = [[[-1, -1]]*M for _ in range(N)]  # 최단거리를 기록하기 위한 배열
    visit[tmin[1]][tmin[2]] = [tmin[1], tmin[2]]
    print("===visit===")
    for i in range(N):
        print(*visit[i])
    print("===check===")
    for i in range(N):
        print(*check[i])
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
            if visit[nx][ny] == [-1, -1]:
                visit[nx][ny] = [x, y]
                q.append((nx, ny))
            
            # 가장 강한 포탑을 만나면
            if lst[nx][ny] == tmax[0]:
                lst[nx][ny] -= tmin[0]
                bx, by = visit[nx][ny]
                while True:
                    if bx==tmin[1] and by==tmin[2]:
                        break
                    lst[bx][by] -= tmin[0]//2
                    bx, by = visit[bx][by]
                print("===visit===")
                for i in range(N):
                    print(*visit[i])
                print("===check===")
                for i in range(N):
                    print(*check[i])
                return



from collections import deque
import sys
N, M, K = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmax = [0, 0, 0]
tmin = [101, 0, 0]
attack = 0  # check에 언제 공격했는지 입력하기 위한 변수
check = [[0]*M for _ in range(N)]  # 언제 공격했는지 확인하는 배열. 값이 클수록 최근
for i in range(N):  # 배열 입력 및 가장 약한 포탑 / 가장 강한 포탑 확인
    for j in range(N):
        # 기존의 최댓값보다 큰 값이 있다면 배열을 아예 새로 만든다
        if lst[i][j] > tmax[0]:
            tmax = [lst[i][j], i, j]
        # 기존의 최댓값과 같은 값이 있다면 차례대로 계산
        elif lst[i][j] == tmax[0]:
            x, y= tmax[1], tmax[2]
            if check[x][y] < check[i][j]:
                tmax = [lst[i][j], i, j]
            elif check[x][y] == check[i][j]:
                if x+y < i+j:
                    tmax = [lst[i][j], i, j]
                elif x+y == i+j:
                    if y < j:
                        tmax = [lst[i][j], i, j]
        
        # 기존의 최솟값보다 작은 값이 있다면 배열을 새로 만든다
        if lst[i][j]>0 and lst[i][j]<tmin[0]:
            tmin = [lst[i][j], i, j]
        # 기존의 최솟값과 같은 값이 있다면 차례대로 계산
        elif lst[i][j] == tmin[0]:
            x, y= tmin[1], tmin[2]
            if check[x][y] > lst[i][j]:
                tmin = [lst[i][j], i, j]
            elif check[x][y] == lst[i][j]:
                if x+y > i+j:
                    tmin = [lst[i][j], i, j]
                elif x+y == i+j:
                    if y > j:
                        tmin = [lst[i][j], i, j]

BFS(tmin)