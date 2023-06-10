# https://www.codetree.ai/training-field/frequent-problems/problems/artistry/description
# 맞닿아 있는 변을 어떻게 구하나?
def BFS(x, y):  # 각 영역은 숫자로 구분한다
    global cnt
    q = deque()
    q.append((x, y))
    visit[x][y] = cnt
    ck[cnt][0] = art[x][y]  # ck에는 각 숫자별로 영역의 넓이를 정하려고 했는데 생각해보니 여기의 숫자와 주어진 숫자를 연결하는걸 못할것 같다
    ck[cnt][1] += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                if art[x][y] == art[nx][ny]:
                    visit[nx][ny] = cnt
                    q.append((nx, ny))
                    ck[cnt][0] = art[nx][ny]
                    ck[cnt][1] += 1

from collections import deque
import sys
n = int(sys.stdin.readline())  # 반드시 홀수
art = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[0]*n for _ in range(n)]
ck = [[0, 0] for _ in range(11)]  # 문제에서 주어지는 숫자는 10이하라고 했다
cnt = 1
for i in range(n):
    for j in range(n):
        if visit[i][j]==0:  # 아직 탐색하지 않은 부분이라면
            BFS(i, j)
            cnt += 1

# 중간 라인 반시계 방향으로 회전
mid = n//2
for i in range(mid+1):
    art[mid-i][mid], art[mid+i][mid], art[mid][mid-i], art[mid][mid+i] = art[mid][mid+i], art[mid][mid-i], art[mid-i][mid], art[mid+i][mid]
# 라인을 기준으로 시계방향으로 어떻게 돌리나?
for i in range(n):
    print(visit[i])