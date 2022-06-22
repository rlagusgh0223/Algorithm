import sys
n, m = map(int, sys.stdin.readline().split())
map = [[int(now) for now in sys.stdin.readline().split()] for _ in range(n)]
type = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def downstreet(x, y):
  if type[x][y] != -1:
    return type[x][y]
  if x==n-1 and y==m-1:
    return 1
  type[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and map[x][y] > map[nx][ny]:
      type[x][y] += downstreet(nx, ny)

  return type[x][y]

print(downstreet(0, 0))