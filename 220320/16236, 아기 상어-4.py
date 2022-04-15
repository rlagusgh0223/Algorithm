from collections import deque
import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now_size = 2

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j    # 함수로 뺀 부분이 아니라 전역변수가 될 것 같아 따로 선언 안해봤다
            array[i][j] = 0

def BFS():
    q = deque()
    q.append((now_x, now_y))
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:    #
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

    return dist

def find(dist):    # 실패
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j

    if min_dist == 1e9:
        return False    # True로 하면 밑에 if문에서 받을때 그냥 value로 둬야하는데 그럼 x,y,min_dist로 리턴할때도 동작하게 되어 무조선 0이 출력된다
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:    # 실패
    value = find(BFS())
    if not value:    # not value로 하고 위에서 return 값을 False로 해야 x,y,min_dist값을 리턴할때 동작 안한다. 그것도 값은 있으므로 not 값을 해야 Flase로 인식한다.
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1

        if ate >= now_size:
            now_size += 1
            ate = 0