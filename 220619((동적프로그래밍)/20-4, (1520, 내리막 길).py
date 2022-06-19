import sys
n, m = map(int, sys.stdin.readline().split())
map = [[int(now) for now in sys.stdin.readline().split()] for _ in range(n)]
chk = [[-1 for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def downstreet(x, y):
  if chk[x][y] != -1:
    return chk[x][y]
  if x==n-1 and y==m-1:
    return 1
  chk[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and map[x][y]>map[nx][ny]:
      chk[x][y] += downstreet(nx,ny)
  return chk[x][y]

print(downstreet(0, 0))