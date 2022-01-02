from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [0] * N
q = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))
S, X, Y = map(int, sys.stdin.readline().split())                # 여기까지 입력을 받는 부분

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:                                    # 그래프에서 0이 아닌 부분, 즉 바이러스에 감염된 부분은
            now = graph[i][j]
            q.append([now, 0, i, j])                            # 바이러스 정보와 위치, 그리고 시간에 따라 카운트 할 수 있도록 0을 입력한다

q.sort()                                                        # 바이러스를 오름차순으로 정렬하고, 큐로 만들어서 먼저 입력한 것들부터 계산하도록 한다
q = deque(q)

while q:                                                        # BFS를 사용하기 위해 q에 값이 있는 동안 반복
    virus, sec, x, y = q.popleft()
    if sec == S:                                                # 단, q에 내용이 있더라도 사용자가 입력한 시간이 되면 종료한다
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus                           # 바이러스와 인접하고 감염이 안된곳은 바이러스에 감염된다
                q.append([virus, sec+1, nx, ny])                # 감염된 방의 바이러스 정보와 위치를 입력하고 1초 더해준다(이렇게 하면 바이러스별로 한 차례 지나갈때마다 1초가 지난걸로 할 수 있다)

print(graph[X-1][Y-1])                                          # 입력된 위치의 바이러스값 출력