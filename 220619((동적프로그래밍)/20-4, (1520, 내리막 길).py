N, M = map(int, input().split())
map = [[int(now) for now in input().split()] for _ in range(N)]
chk = [[-1 for _ in range(M)] for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def downstreet(x, y):
  if chk[x][y] != -1:
    return chk[x][y]
  if x==N-1 and y==M-1:
    return 1
  chk[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and map[x][y] > map[nx][ny]:
      chk[x][y] += downstreet(nx,ny)

  return chk[x][y]

print(downstreet(0,0))