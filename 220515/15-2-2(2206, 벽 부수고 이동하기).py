# 다음문제 14502
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs():
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]    # 해당 지점을 방문했는지, 벽을 부수었는지 저장하기 위한 배열 생성
    visit[0][0][0] = 1    # 처음 위치(0,0)에 벽을 부수지 않은 상태로 방문했으므로 1로 값을 변경한다
    
    while q:
        x, y, wall = q.popleft()    # 큐의 좌표(x, y)와 벽의 상태를 받는다
        if x==(N-1) and y==(M-1):    # x, y 가 목표지점(N-1, M-1)에 도착했다면 
            return visit[x][y][wall]    # 최단거리가 몇인지 확인한다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny][wall]==0:    # 이동할 칸이 맵 안이고, 다음에 이동할 칸을 방문하지 않았다면
                if Map[nx][ny] == '0':    # 이동할 칸의 맵이 0이 아니라면 벽을 부술 수 있는 위치가 아니므로
                    visit[nx][ny][wall] = visit[x][y][wall] + 1    # 다음칸 이동거리, 벽을 부수지 않음 = 현재칸 이동거리+1, 벽을 부수지 않음 으로 설정
                    q.append([nx, ny, wall])    # 큐에 다음 이동 칸과 현재 벽의 상태를 넣어준다
                if wall == 0 and Map[nx][ny] == '1':    # 이동할 칸의 맵이 1이고 벽을 부술 수 있는 상태라면
                    visit[nx][ny][1] = visit[x][y][0] + 1    # 다음 이동칸, 벽을 부숨 = 현재 칸 이동거리+1, 벽을 부수지 않음으로 설정
                    q.append([nx, ny, 1])    # 큐에 다음 이동 칸과, 벽을 부순 상태를 넣어준다
        for i in range(N):
            print(visit[i])
        print("---------------")
    return -1    # 이동할 수 없는 경우에는 -1을 값으로 반환해준다

N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]    # 맵을 입력 받는다
q = deque()
q.append([0, 0, 0])    # 큐에 좌표 (0,0)과 벽을 부수지 않은 상태인 0을 넣어준다
print(bfs())