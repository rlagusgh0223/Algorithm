from collections import deque
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[-1]*m for _ in range(n)]
check = [[True]*m for _ in range(n)]
group_size = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    g = len(group_size)
    group[sx][sy] = g
    check[sx][sy] = False
    q = deque()
    q.append((sx, sy))
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny]==0 and check[nx][ny]:
                    group[nx][ny] = g
                    check[nx][ny] = False
                    q.append((nx, ny))
                    cnt += 1
    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if a[i][j]==0 and check[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<m and a[nx][ny]==0:
                    near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans%10, end='')
    print()