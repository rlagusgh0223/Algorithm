def go(x, y, num, length):
    if length == n+1:
        ans.add(num)
        return
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            go(nx, ny, num*10+a[nx][ny], length+1)

n = 5
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = [list(map(int, input().split())) for _ in range(n)]
ans = set()
for i in range(n):
    for j in range(n):
        go(i, j, a[i][j], 1)
print(len(ans))