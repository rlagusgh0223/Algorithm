def BFS():
    q = deque()
    q.append((0, 0))
    check[0][0] = 1
    while q:
        x, y = q.popleft()
        if x==N-1 and y==M-1:
            return check[x][y]-1
        for i in range(1, a[x][y]+1):
            if x+i<N and check[x+i][y]==0:
                check[x+i][y] = check[x][y] + 1
                q.append((x+i, y))
            if y+i<M and check[x][y+i]==0:
                check[x][y+i] = check[x][y] + 1
                q.append((x, y+i))

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
print(BFS())