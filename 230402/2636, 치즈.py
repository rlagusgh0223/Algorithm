# 다음 부분이 0인 부분(공기인 부분)만 큐에 넣어주고
# 치즈인 부분은 녹여서 그대로 둔다
# 한 시간 뒤에 검사할때 확인하게 된다
def BFS():
    q = deque()
    q.append((0, 0))
    visit = [[0]*c for _ in range(r)]
    visit[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and visit[nx][ny]==0:
                visit[nx][ny] = 1
                if pan[nx][ny] == 0:
                    q.append((nx, ny))
                elif pan[nx][ny] == 1:
                    pan[nx][ny] = 0
                    cnt += 1
    cheese.append(cnt)
    return cnt

from collections import deque
import sys
r, c = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cheese = []
time = 0
while True:
    cnt = BFS()
    if cnt == 0:
        break
    time += 1
print(time)
print(cheese[-2])  # 끝나기 한 시간 전의 치즈 양이니까. -1은 맨 마지막(끝날 당시), -2는 뒤에서 두번째(끝나기 한 시간 전)