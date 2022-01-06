from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
data = [0] * n   # 초기 맵 리스트
temp = [[0 for _ in range(m)] for _ in range(n)]  # 벽을 설치한 뒤의 리스트

for i in range(n):  # 초기 맵 입력
    data[i] = list(map(int, sys.stdin.readline().split()))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0  # 안전영역의 최대 크기를 입력할 변수

# BFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append([nx,ny])

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

# 현재 맵에서 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
# 울타리를 3개 설치한 다음 계속 반복해서 최댓값을 찾는거라 DFS를 쓰는것 같다
def DFS(count):
    global result
    #울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
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