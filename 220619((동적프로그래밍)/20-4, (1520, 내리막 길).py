import sys
N, M = map(int, sys.stdin.readline().split())
map = [[int(now) for now in sys.stdin.readline().split()] for _ in range(N)]
chk = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def down(x, y):
  if chk[x][y] != -1:
    return chk[x][y]
  if x==N-1 and y==M-1:
    return 1
  chk[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and map[x][y] > map[nx][ny]:
      chk[x][y] += down(nx,ny)
  return chk[x][y]

print(down(0,0))