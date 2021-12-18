#뭔소린지 하나도 모르겠다
#아래는 모범답안
n, m = map(int, input().split())
data = []   #초기 맴
temp = [[0] * m for _ in range(n)]  #벽을 설치한 뒤의 맵

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

#바이러스가 사방으로 퍼지도록
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

#안전영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def DFS(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        #각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        
        result = max(result, get_score())
        return

    #빈 공간에 울타리 설치
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

for i in range(n):
    print(data[i])
print()
for i in range(n):
    print(temp[i])

#==========================================================
"""
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

# q = deque()
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 2:
#             q.append([i, j])

# while q:
#     x, y = q.popleft()
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if graph[nx][ny]==0:
#                 graph[nx][ny] = 1

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