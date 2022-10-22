def bfs(x, y):
    q = deque()
    q.append((x, y))
    g = len(group_size)
    group[x][y] = g
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and a[nx][ny]==0 and group[nx][ny]==-1:
                q.append((nx, ny))
                group[nx][ny] = g
                cnt += 1
    group_size.append(cnt)

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
group = [[-1]*M for _ in range(N)]
group_size = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if a[i][j]==0 and group[i][j]==-1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if a[i][j]==0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<N and 0<=ny<M and a[nx][ny]==0:
                    near.add(group[nx][ny])
            ans = 1
            for k in near:
                ans += group_size[k]
            print(ans%10, end='')
    print()