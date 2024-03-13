from collections import deque


def solution(n, m, hole):
    # 지도
    # 이동할 수 있는 곳은 0, 함정은 1
    board = [[0]*(m+1) for _ in range(n+1)]
    # 신발을 안 썼으면 [][][0]에, 썼으면 [][][1]에 입력
    dist = [[[-1, -1] for _ in range(m+1)] for _ in range(n+1)]

    for x, y in hole:
        board[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((1, 1, 0))
    dist[1][1][0] = 0

    while q:
        x, y, cs = q.popleft()
        for i in range(4):
            for s in range(2):
                # 이미 신발을 썼는데 다음 위치도 신발을 써야 갈 수 있는곳이라면
                if cs==1 and s==1:
                    continue
                # s=0일때 다음칸은 신발 없이 그냥 가므로 1칸만(0+1)
                # s=1일때 다음칸은 신발 신고 가므로 2간(1+1) 이동
                # cs|s는 둘 중 하나만 1이어도 1이 되는데
                # 둘 다 1인 경우는 위에서 걸렀으므로 이미 신발을 쓴 경우나
                # 이번에 신발을 쓰고 이동할 경우 ns는 1이 된다
                nx, ny, ns = x+dx[i]*(s+1), y+dy[i]*(s+1), cs|s
                if 1<=nx<=n and 1<=ny<=m and board[nx][ny]==0 and dist[nx][ny][ns]==-1:
                    q.append((nx, ny, ns))
                    dist[nx][ny][ns] = dist[x][y][cs] + 1

    answer = dist[n][m][1]
    if dist[n][m][0] != -1:
        answer = min(answer, dist[n][m][0])

    return answer

import sys

n, m = map(int, sys.stdin.readline().split())
hole = list(sys.stdin.readline().strip().split("], ["))
hole = [list(map(int, now.split(", "))) for now in hole]
print(solution(n, m, hole))