# 모범답안
n, m = map(int, input().split())
data = []   # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]      # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def DFS(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                DFS(count)
                data[i][j] = 0
                count -= 1

DFS(0)
print(result)

#############################################################################################################
# 1. 바이러스 구역(2) 주변에 벽(1)으로 에워싸는건 했으나 3번을 넘기므로 답이 아니다
# 2. 3번만 돌아가도록 코드는 작성했으나 다양한 구역에서 돌아가지는 않음
# 3. 반복문 안에 같은 변수(i)를 사용해서 코드에 혼선이 있었음
# 4. 1번과 2번을 융합하려 시도하였으나 실패
# 5. 어쨌든 벽(1)이 하나도 없으면 대각선으로 벽을 설치하는 방법밖에 없으므로 따로 가정하여 만들려고 했으나 실패
#    1을 설치하는것 까지는 되는데 나머지 필요없는것들을 다시 0으로 만드는게 안됨
# from collections import deque
# import sys

# N, M = map(int, sys.stdin.readline().split())
# graph = [0] * N
# for i in range(N):
#     graph[i] = list(map(int, sys.stdin.readline().split()))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# sx = [1, -1, -1, 1, -2, 2, 0, 0]    # 1이 하나도 없을때 대각선으로 확인하기 위한 리스트
# sy = [1, -1, 1, -1, 0, 0, -2, 2]
# cnt = 0
# q = []                              # 그래프에서 다음 위치 
# one = 0

# X = [0, M-1, 0, M-1]    #1이 하나도 없을때 그래프 끝에를 표시하기 위한 리스트
# Y = [0, 0, N-1, N-1]

# def BFS(x, y):
#     global cnt
#     q = deque()
#     q.append([x, y])
#     graph[x][y] = 1                 #밑에는 다음 것부터 적용되니까 여기서 시작점 1로 바꾸고 카운터 증가
#     cnt += 1
#     while q:
#         x, y = q.popleft()         #시작점 주변에 점검할 숫자가 있는지 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]     
#             if cnt % 3 == 0:
#                 while q:                # while문 나가기 전에 3번 벽 세우면 원상복구
#                     x, y = q.pop()
#                     graph[x][y] = 0
#                 cnt = 0
#             if 0 <= nx < N and 0 <= ny < M:     # 다음 좌표가 그래프 내에 있다면
#                 if graph[nx][ny]==0:            # 다음 좌표도 조정
#                     graph[nx][ny] = 1
#                     cnt += 1
#                     print(nx, ny)
#                     for k in range(N):
#                         print(graph[k])
#                     print()

# def NoOne():                # 1이 하나도 없으면 어차피 대각선으로 구하는것 뿐이니 해보려고 했다
#     #cal = 1
#     oq = deque()
#     for i in range(4):
#         x = X[i]
#         y = Y[i]
#         for j in range(8):
#             nx = x + sx[j]
#             ny = y + sy[j]
#             if 0 <= nx < N and 0 <= ny < M:
#                 # if graph[nx][ny] == 2:
#                 #     #cal = 1
#                 #     print(oq)
#                 #     while oq:
#                 #         x, y = oq.popleft()
#                 #         graph[x][y] = 0

#                 if graph[nx][ny] == 0:
#                     oq.append([nx, ny])
#                     graph[nx][ny] = 1
#                     print(nx, ny)
#                     print()
#                     #cal += 1
#                     #if cal == 3:
#                         #break
#         #if cal == 3:
#             #break

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             one = 1

# for i in range(N):
#     for j in range(M):     
#         if one == 0:
#             NoOne()
#             for k in range(N):
#                 print(graph[k])
#             print()
#             break

#         if cnt % 3 == 0 and one == 1:        #3번 벽을 세운 후 리셋하기 위해
#             while q:
#                 x, y = q.pop()
#                 graph[x][y] = 0
#         if graph[i][j] == 0 and one == 1:        # 그래프에서 0이 발견되면
#             BFS(i, j)               # 1로 바꾸기 위한 함수 호출
#             print("BFS 종료",i, j)  # 호출 후 그래프 확인용
#             for k in range(N):
#                 print(graph[k])
#             print()
#     if one == 0:
#         break

"""
for i in range(N):
    for j in range(M):     
        if cnt % 3 == 0:
            while q:
                x, y = q.pop()
                graph[x][y] = 0
        if graph[i][j] == 0:
            cnt += 1
            print(cnt)
            graph[i][j] = 1
            q.append([i,j])
            for k in range(N):
                print(graph[k])
            print()


================================================
def BFS(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny]==0:
                    graph[nx][ny] = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            BFS(i, j)
for i in range(N):
    print(graph[i])
    for j in range(M):
        if graph[i][j] == 0:
            cnt += 1
print(cnt)
"""