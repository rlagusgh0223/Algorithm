from collections import deque
import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
now_x, now_y = 0, 0    # 아기 상어의 현재 위치를 표시하기 위한 변수
now_size = 2    # 아기 상어의 처음 크기는 2다. 이 숫자만큼 물고기를 먹을때마다 증가

dx = [-1, 1, 0, 0]  #
dy = [0, 0, -1, 1]  #

# 아기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[i][j] = 0

def BFS():
    dist = [[-1 for _ in range(n)] for _ in range(n)]  #
    dist[now_x][now_y] = 0  #
    q = deque()
    q.append((now_x, now_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:    #
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1  #

    return dist

def find(dist):     #
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j

    if min_dist == 1e9:
        return False
    else:
        return x, y, min_dist

result = 0  #
ate = 0     #

while True:     #
    value = find(BFS())
    if not value:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1    # 만약 ate와 now_size가 같다면 현재 크기만큼 먹은거니까 now_size에 1 더해준다
        if ate >= now_size:
            now_size += 1
            ate = 0