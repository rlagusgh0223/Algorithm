# 예제 2번 같은 경우는 처음부터 해당이 안되니까 0이 나와야 되는데 그마저도 안된다
from collections import deque
import sys
N, L, R = map(int, sys.stdin.readline().split())
A = [0] * N

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))

endFlag = False
cnt = 0

def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= nx < N:
            minus = A[nx][ny] - A [x][y]
            if L <= minus <= R:
                DFS(nx, ny)

def BFS(x, y):
    global cnt, endFlag
    now = 0
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                now = A[nx][ny] = A[x][y]
                if L <= abs(now) <= R:
                    q.append([nx, ny])
                    endFlag = True
    if endFlag:         # 만약 인접 국가가 하나도 없다면 0이 나오도록
        cnt += 1

BFS(0,0)
print(cnt)