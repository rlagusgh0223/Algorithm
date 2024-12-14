from collections import deque


def solution(maze):
    n, m = len(maze), len(maze[0])
    red = [[True]*m for _ in range(n)]
    blue = [[True]*m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx, ry = i, j
            elif maze[i][j] == 2:
                bx, by = i, j
    
    q = deque()
    q.append((rx, ry, bx, by, red, blue, 0))
    while q:
        rx, ry, bx, by, red, blue, cnt = q.popleft()
        red[rx][ry] = False
        blue[bx][by] = False
        #####
        print(rx, ry, bx, by, cnt)
        for i in range(n):
            print(red[i])
        print()
        for i in range(n):
            print(blue[i])
        #####
        if maze[rx][ry]==3 and maze[bx][by]==4:
            return cnt
        elif maze[rx][ry]==3:
            red_end = True
        elif maze[bx][by]==4:
            blue_end = True
        else:
            red_end, blue_end = False, False
        
        for i in range(4):
            # 빨간 수레는 도착했을때
            if red_end:
                nbx, nby = bx+dx[i], by+dy[i]
                if 0<=nbx<n and 0<=nby<m and maze[nbx][nby]<5 and blue[nbx][nby]:
                    # 다음 파란 수레 위치가 빨간 수레 위치면 못 간다
                    if nbx==rx and nby==ry:
                        continue
                    q.append((rx, ry, nbx, nby, red, blue, cnt+1))
            # 파란 수레는 도착했을때때
            elif blue_end:
                nrx, nry = rx+dx[i], ry+dy[i]
                if 0<=nrx<n and 0<=nry<m and maze[nrx][nry]<5 and red[nrx][nry]:
                    # 다음 빨간 수레 위치가 파란 수레 위치면 못간다
                    if nrx==bx and nry==by:
                        continue
                    q.append((nrx, nry, bx, by, red, blue, cnt+1))
            # 둘 다 도착하지 못했을때때
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