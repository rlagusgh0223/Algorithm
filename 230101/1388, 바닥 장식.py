# dfs가 더 빠르고 코드도 짧다

# def dfs(i, j):
#     check[i][j] = 1
#     if j+1<M and ground[i][j]=='-' and ground[i][j+1]=='-':
#         dfs(i, j+1)
#     elif i+1<N and ground[i][j]=='|' and ground[i+1][j]=='|':
#         dfs(i+1, j)

from collections import deque
def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        check[i][j] = 1
        if j+1<M and ground[i][j]=='-' and ground[i][j+1]=='-':
            q.append((i, j+1))
        elif i+1<N and ground[i][j]=='|' and ground[i+1][j]=='|':
            q.append((i+1, j))

import sys
N, M = map(int, sys.stdin.readline().split())
ground = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
check = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            # dfs(i, j)
            bfs(i, j)
            cnt += 1
print(cnt)