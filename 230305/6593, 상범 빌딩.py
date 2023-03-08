# 나는 상하의 경우가 동서남북과 다른 경우라고 생각해서 조건문을 따로 만들었는데
# 남들은 그냥 6개씩 나머지는 0으로 해서 한번에 조건문을 만들었다
# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
# for i in range(6):
# 이런식으로 했다면 코드가 더 간결해졌을것이다.
def BFS(i, j, k):
    q = deque()
    build[i][j][k] = 0
    q.append((i, j, k))
    while q:
        l, x, y = q.popleft()
        for i in range(2):
            nl = l + dl[i]
            if 0 <= nl < L:
                if build[nl][x][y]=='.':
                    q.append((nl, x, y))
                    build[nl][x][y] = build[l][x][y] + 1
                elif build[nl][x][y] == 'E':
                    return build[l][x][y] + 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if build[l][nx][ny]=='.':
                    q.append((l, nx, ny))
                    build[l][nx][ny] = build[l][x][y] + 1
                elif build[l][nx][ny] == 'E':
                    return build[l][x][y] + 1
    return 0

from collections import deque
import sys
dl = [-1, 1]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == R == C == 0:
        break
    build = [[] for _ in range(L)]
    for i in range(L):
        build[i] = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        x = sys.stdin.readline()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if build[i][j][k] == 'S':
                    now = BFS(i, j, k)
                    if now == 0:
                        print("Trapped!")
                    else:
                        print("Escaped in {} minute(s).".format(now))