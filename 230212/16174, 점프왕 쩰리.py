def BFS():
    q = deque()
    q.append((0, 0))
    check[0][0] = 1
    while q:
        x, y = q.popleft()
        if ground[x][y] == -1:
            return "HaruHaru"
        if 0<=x+ground[x][y]<N and check[x+ground[x][y]][y]==0:
            q.append((x+ground[x][y], y))
            check[x+ground[x][y]][y] = 1
        if 0<=y+ground[x][y]<N and check[x][y+ground[x][y]]==0:
            q.append((x, y+ground[x][y]))
            check[x][y+ground[x][y]] = 1
    return "Hing"

from collections import deque
import sys
N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
print(BFS())