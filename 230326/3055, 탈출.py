# 인터넷에 보면 다른 코드도 많은데 대부분 함수 2개 돌리고
# 내 코드도 시간은 그렇게 느리지 않은것 같아서 그냥 내 코드만 올린다

def WBFS(i, j):
    q = deque()
    q.append((i, j))
    check[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and ground[nx][ny]=='.':
                if check[nx][ny]==-1 or check[x][y] < check[nx][ny]-1:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

def BFS(i, j):
    q = deque()
    q.append((i, j))
    check[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if ground[nx][ny]=='.' and (check[nx][ny]==-1 or check[x][y] < check[nx][ny]-1):
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1
                if ground[nx][ny] == 'D':
                    return check[x][y]+1
    return "KAKTUS"

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())
ground = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
check = [[-1]*C for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(R):
    for j in range(C):
        if ground[i][j] == '*':
            WBFS(i, j)
for i in range(R):
    for j in range(C):
        if ground[i][j] == 'S':
            print(BFS(i, j))