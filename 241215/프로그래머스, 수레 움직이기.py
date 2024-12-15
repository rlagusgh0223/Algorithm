import copy
from collections import deque


def solution(maze):
    n, m = len(maze), len(maze[0])
    # 각 수레들이 지나간곳을 저장할 리스트
    red = [[True]*m for _ in range(n)]
    blue = [[True]*m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 빨간수레, 파란수레 출발 위치치
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx, ry = i, j
            elif maze[i][j] == 2:
                bx, by = i, j
    
    q = deque()
    # 빨간수레 위치(x,y) 파란수레위치(x,y), 빨간수레 지나간곳, 파란수레 지나간곳, 지금까지 이동횟수
    q.append((rx, ry, bx, by, red, blue, 0))
    while q:
        rx, ry, bx, by, RED, BLUE, cnt = q.popleft()

        # 파이썬은 리스트를 참조로 전달하기 때문에
        # deepcopy를 이용해 리스트를 복사하지 않고 그대로 넘기면
        # 다른 큐에서 해당 리스트가 변경된 상태로 반영된다
        red = copy.deepcopy(RED)
        blue = copy.deepcopy(BLUE)

        # 수레가 지나간 곳은 이제 못 가도록 False 입력
        red[rx][ry] = False
        blue[bx][by] = False

        # 둘 다 도착하면 지금까지 사용한 턴 리턴
        if maze[rx][ry]==3 and maze[bx][by]==4:
            return cnt
        # 빨간 수레만 도착했을때
        elif maze[rx][ry]==3:
            red_end = True
        # 파란 수레만 도착했을때
        elif maze[bx][by]==4:
            blue_end = True
        # 둘다 도착하지 않았을때
        # 이전 popleft에서 빨간수레나 파란수레만 도착했으나
        # 이번 popleft에는 둘 다 도착 못한 경우일 수 있다
        else:
            red_end, blue_end = False, False
        
        # 경로찾기(미로 길이 최대 4x4)
        for i in range(4):
            # 빨간 수레는 도착했을때
            if red_end:
                nbx, nby = bx+dx[i], by+dy[i]
                if 0<=nbx<n and 0<=nby<m and maze[nbx][nby]<5 and blue[nbx][nby]:
                    # 다음 파란 수레 위치가 빨간 수레 위치면 못 간다
                    if nbx==rx and nby==ry:
                        continue
                    q.append((rx, ry, nbx, nby, red, blue, cnt+1))
            # 파란 수레는 도착했을때
            elif blue_end:
                nrx, nry = rx+dx[i], ry+dy[i]
                if 0<=nrx<n and 0<=nry<m and maze[nrx][nry]<5 and red[nrx][nry]:
                    # 다음 빨간 수레 위치가 파란 수레 위치면 못간다
                    if nrx==bx and nry==by:
                        continue
                    q.append((nrx, nry, bx, by, red, blue, cnt+1))
            # 둘 다 도착하지 못했을때
            else:
                nrx, nry = rx+dx[i], ry+dy[i]
                if 0<=nrx<n and 0<=nry<m and maze[nrx][nry]<5 and red[nrx][nry]:
                    for j in range(4):
                        nbx, nby = bx+dx[j], by+dy[j]
                        if 0<=nbx<n and 0<=nby<m and maze[nbx][nby]<5 and blue[nbx][nby]:
                            # 다음 위치가 같으면 못 간다
                            if nrx==nbx and nry==nby:
                                continue
                            # 두 수레의 위치가 바뀌는거면 못 간다
                            elif (rx==nbx and ry==nby) and (bx==nrx and by==nry):
                                continue
                            q.append((nrx, nry, nbx, nby, red, blue, cnt+1))

    return 0


import sys

maze = list(sys.stdin.readline().strip().split("], ["))
maze = [list(map(int, m.split(", "))) for m in maze]
print(solution(maze))