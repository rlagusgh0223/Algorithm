from collections import deque
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
check = [[-1]*N for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
q = deque()
q.append((r1, c1))
check[r1][c1] = 0
while q:
    x, y = q.popleft()
    for i in range(6):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and check[nx][ny]==-1:
            q.append((nx, ny))
            check[nx][ny] = check[x][y] + 1
print(check[r2][c2])