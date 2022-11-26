n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a = [[0]*(m+2)] + [[0]+row+[0] for row in a] + [[0]*(m+2)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 2*n*m
for x in range(1, n+1):
    for y in range(1, m+1):
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if a[x][y] > a[nx][ny]:
                ans += a[x][y] - a[nx][ny]
print(ans)