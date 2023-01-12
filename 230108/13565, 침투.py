from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
lab = [[int(now) for now in input().rstrip()] for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = deque()
for i in range(N):
    if lab[0][i] == 0:
        q.append((0, i))
        lab[0][i] = 2
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and lab[nx][ny]==0:
            lab[nx][ny] = 2
            q.append((nx, ny))
if lab[M-1].count(2) > 0:
    print("YES")
else:
    print("NO")