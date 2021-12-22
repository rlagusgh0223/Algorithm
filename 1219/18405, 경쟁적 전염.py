from collections import deque
import numpy as np                  # reshape를 쓰기 위한 입력
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

check = list(map(int, sys.stdin.readline().split()))    # 입력의 마지막 줄 을 받기 위한 리스트(몇 초 후 어느 좌표)
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = np.reshape(graph,(1,-1))      # 입력 받은 리스트를 한줄로 만들기(입력이 2차원 배열이라 그런가 2차원 배열이 된다)
ans = deque(set(ans[0]))            # 집합을 이용해 중복된 숫자 없애고 오름차순으로 만든 배열을 큐로 만들어준다(리스트도 상관없으나 편하게 맨 앞의 수를 지우기 위해 큐 사용)
ans.popleft()                       # 큐의 맨 처음은 0이니까 0을 빼고 나머지 바이러스들만 큐에 들어있게 한다

for cnt in ans:                     # 바이러스 종류만큼 반복하여 그래프에 있는 바이러스 좌표 q에 입력
    for i in range(N):
        for j in range(K):
            if graph[i][j] == cnt:
                q.append([i,j])

sec = check[0]
for _ in range(sec):                # 입력에 주어진 초 만큼
    for cnt in ans:                 # 바이러스 순서대로 전염
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < K:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = cnt
                    q.append([nx, ny])

x = check[1] - 1                    # 입력에서 주어진 좌표의 수 출력
y = check[2] - 1
print(graph[x][y])