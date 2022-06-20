n, m = map(int, input().split())
map = [list(map(int, input().split())) for i in range(n)]
chk = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def down(x, y):
  if chk[x][y] != -1:
    return chk[x][y]
  if x==n-1 and y==m-1:
    return 1
  chk[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and map[x][y]>map[nx][ny]:
      chk[x][y] += down(nx, ny)
  return chk[x][y]

print(down(0, 0))