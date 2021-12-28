# 답은 나오는데 틀렸다고 한다. 왜?
from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chk1, chk2, chk3 = map(int, sys.stdin.readline().split())    # 입력의 마지막 줄 을 받기 위한 리스트(몇 초 후 어느 좌표)

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = []                            # 바이러스 순서를 정리하기 위한 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:        # 바이러스가 있는 위치는 다 입력받는다
            now = graph[i][j]
            ans.append(now)
ans.sort()

for cnt in ans:                     # 바이러스 종류만큼 반복하여 그래프에 있는 바이러스 좌표 q에 입력
    for i in range(N):
        for j in range(N):
            if graph[i][j] == cnt:  # 바이러스 순서대로 q에 좌표 입력됨
                q.append([cnt, 0, i, j])

#chk = 0
while q:
    # if sec == chk1:
    #     break
    # for cnt in ans:         #모범답안에서는 이 부분을 없애고 q에 따로 입력해서 넣은것 같은데 무슨 차이가 있는건지 모르겠다 한번 이 코드에서 여기만 바꿔서 해보겠다
    virus, sec, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                q.append([virus, sec+1, nx, ny])
    #chk += 1

#print(graph)

x = chk2 - 1                    # 입력에서 주어진 좌표의 수 출력
y = chk3 - 1                    # 0으로 리스트를 만들었으니 바이러스가 전염되지 않았으면 자동으로 0이 나옴
print(graph[x][y])