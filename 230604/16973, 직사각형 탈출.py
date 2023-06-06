# 직사각형 안에 벽이 있는지 확인
# 이 부분을 BFS나 main에 두면 시간초과 나온다
def check(x, y):
    for r, c in walls:
        if x<=r<=x+H and y<=c<=y+W:
            return False
    return True

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx==Fr and ny==Fc:
                return visit[x][y]
            if 0<=nx<N-H and 0<=ny<M-W and visit[nx][ny]==0:
                if check(nx, ny):
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
    return -1

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
H, W, Sr, Sc, Fr, Fc = H-1, W-1, Sr-1, Sc-1, Fr-1, Fc-1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 벽의 위치 탐색 및 저장
walls = []
for i in range(N):
    for j in range(M):
        if pan[i][j] == 1:
            walls.append((i, j))
visit = [[0]*M for _ in range(N)]  # 직사각형의 맨 왼쪽 위 부분이 지나간 적이 있는지 확인하는 리스트
print(BFS(Sr, Sc))