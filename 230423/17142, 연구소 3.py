def BFS():
    global num
    maxx = 0  # 이번 계산에서 전염 마친 최종 시간을 저장하기 위한 변수
    eNum = 0  # 이번 계산에서 전염 구역 저장하기 위한 변수
    while q:  # 바이러스 전염 구역이 있다면 계속
        x, y, now = q.popleft()  # 바이러스의 x, y, 최소시간 입력
        maxx = max(maxx, now)  # 최종시간을 maxx에 입력
        if eNum >= emptyCnt:  # 전염구역이 전염 가능구역만큼 전염했다면 더이상 할 필요가 없으므로 이번턴 종료
            continue
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if mmap[nx][ny]!=1 and mvisited[nx][ny]!=num:  # 다음 구간이 벽이 아니고 이번 턴에 방문하지 않았다면
                mvisited[nx][ny] = num  # 이번 턴에 방문했다고 체크하고
                if mmap[nx][ny]==0:  # 전염 가능 구간이라면
                    eNum += 1  # 전염했다고 체크
                q.append([nx, ny, now+1])  # 다음 좌표와 그 좌표의 최소시간 입력한다
    if eNum < emptyCnt:  # 만약 모든 구간을 전염시키지 못했다면 -1 리턴
        return -1
    return maxx  # 아니라면 최종시간 리턴

def DFS(depth, idx):
    global num, ans
    if depth == M:  # 전파 가능한 모든 바이러스가 전파를 했다면 이제 계산을 해야되므로
        num += 1  # 방문 체크를 하기 위한 변수에 1 증가
        for i in range(len(virus)):  # 바이러스의 수 만큼 반복하며
            if vvisited[i] == 1:  # 만약 이번 바이러스가 활성화 바이러스라면
                q.append([virus[i][0], virus[i][1], 0])  # x좌표, y좌표, 현재까지 최소 시간 입력(여기서는 발원지니까 시간이 0이다)
        nowCnt = BFS()
        if nowCnt!=-1 and ans>nowCnt:  # 모든 구간을 전염시킨 최소시간이 지금까지 최소시간보다 작다면
            ans = nowCnt  # 최소시간 변경 후 리턴
            return
    for i in range(idx, len(virus)):  # N과 M에서 중복 없고 순서 있는 반복문
        if vvisited[i] == 0:
            vvisited[i] = 1
            DFS(depth+1, i+1)
            vvisited[i] = 0

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
mmap = []  # 연구소를 입력받기 위한 배열
mvisited = [[0]*N for _ in range(N)]
vvisited = [0] * 11  # 바이러스의 개수는 10개까지다
q = deque()
virus = []  # 초기 바이러스 위치를 받기 위한 배열
ans = N*N  # 최소 시간을 저장하기 위한 변수
num = 0  # 해당 depth에 방문했는지 지정하기 위한 변수
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
emptyCnt = 0  # 바이러스가 더 침투할 공간이 있는지 체크하는 변수

for i in range(N):
    mmap.append(list(map(int, sys.stdin.readline().split())))  # 연구소 상태 입력
    for j in range(N):
        if mmap[i][j] == 2:  # 바이러스라면
            virus.append([i, j])  # 바이러스 위치 입력
        elif mmap[i][j] == 0:  # 전염 가능 구역이라면
            emptyCnt += 1  # 가능 구간 수 체크
if emptyCnt == 0:  # 만약 전염 가능한 구역이 없다면
    print(0)  # 어차피 더 할거 없으므로 0 출력하고 종료
    exit()
DFS(0, 0)  # 점검한 곳도 없고 처음이니 depth와 idx 0으로 DFS호출
if ans == N*N:  # 모든 빈칸에 바이러스를 퍼트리지 못할 경우 -1 출력
    print(-1)
else:
    print(ans)  # 모든 빈칸을 전염한 시간 중 최소 시간 출력