from collections import deque


def solution(n, m, hole):
    board = [[0]*(m+1) for _ in range(n+1)]  # 함정이 있는 곳을 표시할 지도
    visit = [[[-1, -1] for _ in range(m+1)] for _ in range(n+1)]  # 신발을 쓰지 않거나 쓰고 방문했는지, 했다면 거리는 얼마인지 입력할 리스트
    for x, y in hole:
        board[x][y] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((1, 1, 0))
    visit[1][1][0] = 0

    while q:
        x, y, cs = q.popleft()  # x좌표, y좌표, 신발 사용 여부
        for i in range(4):
            for s in range(2):
                # 이미 신발을 썼는데 또 쓸 수 는 없다
                if cs==1 and s==1:
                    continue
                # 신발을 쓸 경우 2칸씩 이동하므로 (0+1), (1+1) 칸씩 이동하게 한다
                # |은 or연산이라 cs나 s 둘 중 하나만 1이어도 1이 된다
                # 이 연산을 위해 s를 0, 1로 받는다
                nx, ny, ns = x+dx[i]*(s+1), y+dy[i]*(s+1), cs|s
                if 1<=nx<=n and 1<=ny<=m and board[nx][ny]==0 and visit[nx][ny][ns]==-1:
                    visit[nx][ny][ns] = visit[x][y][cs] + 1
                    q.append((nx, ny, ns))

    answer = visit[n][m][0]
    # visit[n][m][0]이
    # -1이면 무조건 visit[n][m][1]을 따르고
    # -1이 아니면 visit[n][m][1]이 -1이 아닐 경우
    # visit[n][m][0]과 visit[n][m][1] 중 작은 값을 입력한다
    if answer==-1 or (visit[n][m][1]!=-1 and visit[n][m][1]<answer):
        answer = visit[n][m][1]
    return answer


import sys

n, m = map(int, sys.stdin.readline().split())
hole = list(sys.stdin.readline().strip().split("], ["))
hole = [list(map(int, h.split(", "))) for h in hole]
print(solution(n, m, hole))