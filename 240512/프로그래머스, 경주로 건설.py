import sys
from collections import deque


def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def BFS(dir):
        l = len(board)
        visit = [[sys.maxsize]*l for _ in range(l) ]
        q = deque()
        q.append((dir, 0, 0, 0))  # 방향, x좌표, y좌표, 현재까지 값
        while q:
            dir, x, y, cost = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<l and 0<=ny<l and board[nx][ny]==0:
                    if dir == i:
                        ncost = cost + 100
                    else:
                        # 코너를 만드는 값 + 직선경로
                        ncost = cost + 600
                    # cost없이 visit[nx][ny]에 바로 값을 입력하면
                    # 방향과 그에 따른 값이 다를 수 있다
                    # ex) 코너를 이용해서 왔으면 그 값이 적용되야 하는데
                    # 단순히 최소값을 입력하면 visit에는 직선경로의 값이 적용된다
                    if ncost < visit[nx][ny]:
                        visit[nx][ny] = ncost
                        q.append((i, nx, ny, ncost))
        return visit[-1][-1]
    # BFS로 따로 시작하지 않고 (1,0,0,0), (2,0,0,0)을 한번에 append할 경우
    # 서로의 값이 같은 부분이 나왔을때 둘 중 하나의 경로가 사라진다
    # 더 작은 값만 새로 입력되니까
    return min(BFS(1), BFS(2))







board = list(sys.stdin.readline().strip().split("],["))
board = [list(map(int, b.split(","))) for b in board]
print(solution(board))