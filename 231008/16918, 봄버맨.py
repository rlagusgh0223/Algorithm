def BFS(q):
    global ground
    while q:
        x, y = q.popleft()
        ground[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and ground[nx][ny]=='O':
                ground[nx][ny] = '.'

# 폭탄이 터질 타이밍인지, 아닌지 확인
# 폭탄이 터질 타이밍이면 BFS로 폭탄을 터트리고,
# 아니면 폭탄을 설치한다
def check(time):
    global ground
    if time%2 == 1:
        # 폭탄은 3초 후부터 터지므로 처음 1초에는 터지지 않는다
        if time > 1:
            BFS(q)
        for i in range(R):
            for j in range(C):
                if ground[i][j] == 'O':
                    q.append((i, j))
    # 짝수 초 후에는 빈칸에 모두 폭탄을 설치한다
    # 폭탄의 좌표는 이전 순서에 입력해 뒀다
    else:
        ground = [['O']*C for _ in range(R)]

from collections import deque
import sys
R, C, N = map(int, sys.stdin.readline().split())
ground = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
for i in range(1, N+1):
    check(i)
for i in range(R):
    print(*ground[i], sep='')