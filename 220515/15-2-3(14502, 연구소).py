# 모범답안은 시간초과로 pypy3를 해야 답을 맞춘다
# 경호가 알려준 코드로 공부하겠다

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
temp = [[0 for _ in range(m)] for _ in range(n)]    # 벽을 설치한 뒤의 리스트

for i in range(n):    # 초기 맵 입력
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0    # 안전영역의 최대 크기를 입력할 변수

def BFS(x, y):    # BFS를 이용해 바이러스가 사방으로 퍼지게 하기
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append([nx, ny])

# 현재 맵에서 영역의 크기를 계산하는 메서드
def get_score():
    global ans
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    ans = max(ans, score)

# DFS를 이용해 벽을 설치하면서, 매번 안전 영역의 크기 계산
def DFS(depth, x, y):
    if depth == 3:    # 벽을 3개 설치한 경우
        for i in range(n):    # temp에 graph값 전달
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):    # 전달받은 temp에서 바이러스가 검출되면
                if temp[i][j] == 2:
                    BFS(i, j)    # BFS를 이용해서 거기서부터 바이러스가 증가
        get_score()    # 바이러스 전파가 끝나면 칸 수 계산
        return

    for i in range(x, n):
        if i == x:    # 맨 처음에
            for j in range(y+1,m):    # 그래프 전부 채울때까지
                if graph[i][j] == 0:    # 그래프에 벽을 세우며 DFS
                    graph[i][j] = 1
                    DFS(depth+1, i, j)
                    graph[i][j] = 0
        else:
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    DFS(depth+1, i, j)
                    graph[i][j] = 0

DFS(0,0,-1)
print(ans)