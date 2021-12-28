
# from collections import deque
# n, k = map(int, input().split())
# graph = []  #전체 보드 정보를 담는 리스트
# data = []   #바이러스에 대한 정보를 담는 리스트

# for i in range(n):
#     #보드 정보를 한 줄 단위로 입력
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         # 해당 위치에 바이러스가 존재하는 경우
#         if graph[i][j] != 0:
#             #바이러스 종류, 시간, 위치x, 위치y 삽입
#             data.append((graph[i][j], 0, i, j))

# # 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
# data.sort()
# q = deque(data)

# target_s, target_x, target_y = map(int, input().split())

# #바이러스가 퍼져나갈 수 있는 4가지 위치
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 너비 우선 탐색형(BFS) 진행
# while q:
#     virus, s, x, y = q.popleft()
#     # 정확히 s 초가 지나거나, 큐가 빌 때까지 반복
#     if s == target_s:
#         break
#     # 현재 노드에서 주변 4가지 위치로 이동할 수 있는 경우
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 해당 위치로 이동할 수 있는 경우
#         if 0 <= nx < n and 0 <= ny < n:
#             # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(graph[target_x - 1][target_y - 1])

###########################################
# 여기서부터 내 코드
from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chk1, chk2, chk3 = map(int, sys.stdin.readline().split())    # 입력의 마지막 줄 을 받기 위한 리스트(몇 초 후 어느 좌표)

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# ans = 0
# for i in range(N):
#     now = max(graph[i])
#     ans = max(ans, now)

#바이러스값 찾는 코드1
ans = []                            # 바이러스 순서를 정리하기 위한 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:        # 바이러스가 있는 위치는 다 입력받는다
            now = graph[i][j]
            ans.append(now)
ans.sort()

# 바이러스값 찾는 코드2(reshape사용)
# import numpy as np
# ans = np.reshape(graph, N*N)        # 입력 받은 리스트를 한줄로 만들기
# print(ans)
# ans = deque(set(ans))               # 집합을 이용해 중복된 숫자 없애고 오름차순으로 만든 배열을 큐로 만들어준다(리스트도 상관없으나 편하게 맨 앞의 수를 지우기 위해 큐 사용)
# ans.popleft()                       # 큐의 맨 처음은 0이니까 0을 빼고 나머지 바이러스들만 큐에 들어있게 한다

#for cnt in range(1, ans+1):                     # 바이러스 종류만큼 반복하여 그래프에 있는 바이러스 좌표 q에 입력
for cnt in ans:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == cnt:  # 바이러스 순서대로 q에 좌표 입력됨
                q.append([i,j])

chk = 0
while q:
    if chk == chk1:
        break
    #for cnt in range(1, ans+1):                 # 바이러스 순서대로 전염
    for cnt in ans:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    q.append([nx, ny])
    chk += 1

print(graph)

x = chk2 - 1                    # 입력에서 주어진 좌표의 수 출력
y = chk3 - 1                    # 0으로 리스트를 만들었으니 바이러스가 전염되지 않았으면 자동으로 0이 나옴
print(graph[x][y])

#########################################################
"""
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

ans = np.reshape(graph, N*K)        # 입력 받은 리스트를 한줄로 만들기(입력이 2차원 배열이라 그런가 2차원 배열이 된다)
ans = deque(set(ans))               # 집합을 이용해 중복된 숫자 없애고 오름차순으로 만든 배열을 큐로 만들어준다(리스트도 상관없으나 편하게 맨 앞의 수를 지우기 위해 큐 사용)
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
"""