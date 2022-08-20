from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def BFS():
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]    # 해당 지점을 방문했는지, 벽을 부수었는지 저장하기 위한 3차원 배열
    visit[0][0][0] = 1    # 처음 (0, 0) 위치에 벽을 부수지 않은 상태를 방문했으므로 1로 값을 변경한다
    while q:
        x, y, wall = q.popleft()    # 큐의 전단(x, y)와 벽의 상태 획득
        if x==(N-1) and y==(M-1):    # x, y가 목표지점에 도달했다면
            return visit[x][y][wall]    # 최단거리가 몇인지 확인한다
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<M and visit[x+dx[i]][y+dy[i]][wall]==0:    # 범위 내이며 다음칸을 방문하지 않았다면
                if Map[x+dx[i]][y+dy[i]] =='0':    # 이동할 칸의 맵이 0이라면 벽을 부술 수 있는 위치가 아니므로
                    visit[x+dx[i]][y+dy[i]][wall] = visit[x][y][wall]+1    # 현재 칸 이동거리+1, 벽을 부수지 않음으로 설정하고
                    q.append([x+dx[i], y+dy[i], wall])    # 큐에 다음 이동 칸과 현재 벽의 상태를 넣어준다.
                if wall==0 and Map[x+dx[i]][y+dy[i]]=='1':    # 이동할 칸의 맵이 1이고 벽을 부술 수 있는 상태라면
                    visit[x+dx[i]][y+dy[i]][1] = visit[x][y][0] + 1    # 현재 칸 이동거리+1, 벽을 부수지 않음으로 설정하고
                    q.append([x+dx[i], y+dy[i], 1])    # 큐에 다음 이동 칸과 벽을 부순 상태를 넣어준다
    return -1    # 이동할 수 없는 경우에는 -1로 출력한다

N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
q = deque()
q.append([0, 0, 0])
print(BFS())