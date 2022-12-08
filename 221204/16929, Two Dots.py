def go(x, y, bx, by, color):
    if check[x][y]:
        return True
    check[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if (nx, ny) == (bx, by):
                continue
            if a[nx][ny]==color and go(nx, ny, x, y, color):
                return True
    return False

N, M = map(int, input().split())
a = [input() for _ in range(N)]
check = [[False]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    for j in range(M):
        if check[i][j]:
            continue
        ok = go(i, j, -1, -1, a[i][j])
        if ok:
            print("Yes")
            exit()
print("No")