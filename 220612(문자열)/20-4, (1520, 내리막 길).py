# pypy3로 해야 맞는다
m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]    # 이후에 함수에서 방문한 좌표를 다시 방문하지 않도록 -1로 채운다
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dp_bruteForce(y, x):
  if dp[y][x] != -1:    # dp값이 -1이 아니라면 방문한 곳이므로 리턴해준다
    return dp[y][x]
  if y==m-1 and x==n-1:    # (m-1, n-1)좌표에 도달했다면 1을 리턴해준다
    return 1
  dp[y][x]=0    # 방문했음을 나타내기 위해 -1을 0으로 바꿔준다
  for i in range(4):
    dy = y+move[i][0]
    dx = x+move[i][1]
    if 0<=dy<m and 0<=dx<n and map[y][x]>map[dy][dx]:
      dp[y][x] += dp_bruteForce(dy, dx)

  return dp[y][x]

print(dp_bruteForce(0, 0))