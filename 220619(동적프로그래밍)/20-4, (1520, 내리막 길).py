import sys
N, M = map(int, sys.stdin.readline().split())
map = [[int(now) for now in sys.stdin.readline().split()] for _ in range(N)]    # 지도 입력
chk = [[-1 for _ in range(M)] for _ in range(N)]    # 방문한 좌표를 구분하기 위해 -1로 지도 만큼 리스트 생성

dx = [-1, 0, 1, 0]    # 상, 하, 좌, 우를 보기 위한 x, y 좌표
dy = [0, 1, 0, -1]

def downstreet(x, y):    # 완전탐색 함수
  if chk[x][y] != -1:    # -1이 아니라면 방문한 점이므로 반환해준다
    return chk[x][y]
  if x==N-1 and y==M-1:    # 종착지에 도달했다면 1을 반환해준다
    return 1
  chk[x][y] = 0    # 해당 좌표는 방문했다는 뜻으로 0으로 설정해둔다
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and map[x][y]>map[nx][ny]:    # map 안에 있는 좌표이고 다음 좌표가 더 작다면(내리막길이라면)
      chk[x][y] += downstreet(nx, ny)    # 현재좌표의 chk값에 이동가능한 좌표들의 chk값을 계속 더해준다. 방문한 값이라면 해당 chk값을 반환하고(첫번째 if) 마지막에 도착했다면 1을 증가시켜준다(두번째 if)
  return chk[x][y]

print(downstreet(0, 0))