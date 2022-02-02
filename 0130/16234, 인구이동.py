from collections import deque
import sys

# 땅의 크기 N, 인구차이 L, R 입력
N, L, R = map(int, sys.stdin.readline().split())

graph = [0 for _ in range(N)]   # 땅의 인구를 받기 위한 리스트

for i in range(N):  # 땅의 인구 입력
    graph[i] = list(map(int, sys.stdin.readline().split()))

flag = True     # 인구 이동이 종료될때까지 반복해야 하므로, 인구이동이 있었는지 체크하는 변수
ans = -1        # 인구 이동 횟수를 기록하기 위한 변수인데 인구이동이 아예 없는 경우도 있으니 -1에서 시작한다
united = 0  # 연합한 국가인지 분간하고 연합이 여러개일 경우 구분하기 위한 변수

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 확인하기 위한 좌표 리스트
dy = [0, 0, -1, 1]

def open(x, y):     # 인구이동이 가능한 구간인지 확인
    global flag
    global visited
    for i in range(4):      # 사방 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:     # 그래프 범위 안이고
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == 0:     # 인구이동이 가능한 인구차이며 방문한 적이 없다면
                flag = True     # 인구이동 할 수 있으므로 한번 더 반복하도록 True 설정
                return True     # 인구이동 할 수 있다고 판단
    return False    # 인구이동 할수 없다고 판단

def BFS(x,y):
    global visited
    sum = graph[x][y]   # 인구이동의 총합을 나눠야 되므로 총합을 구하기 위해 인구 총합 변수 선언 및 출발위치의 나라 인구수 저장
    cnt = 1     # 인구이동 가능한 나라의 개수 카운트
    q = deque()     # 실질적으로 인구이동을 하려는 큐 선언 및 출발점 입력
    q.append([x,y])
    unitedq = deque()   # 나중에 인구를 나눠서 배분하기 위해 인구 총합한 구역 표시하기 위한 큐
    unitedq.append((x,y))
    visited[x][y] = 1   # 출발지 방문했으므로 1 입력

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if  L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == 0:    # 인구 이동 가능 구역이고 방문한 적 없다면
                    visited[nx][ny] = 1     # 방문 표시
                    q.append((nx,ny))
                    sum += graph[nx][ny]    # 연합 내 총 인구수 계산
                    cnt += 1    # 연합에 들어간 국가 계산
                    unitedq.append((nx,ny))
    while unitedq:      # 인구 이동 종료 후 인구를 해당 연합 국가에 동일하게 분산
        r,c = unitedq.popleft()
        graph[r][c] = sum//cnt

while flag:
    flag = False    # 우선 flag에 False를 줘서 인구이동이 있는한 계속 반복하게 한다
    ans += 1        # 이동 횟수를 더한다(없으면 처음에 -1을 입력했으니까 0으로 나온다)
    visited = [[0 for _ in range(N)] for _ in range(N)]     # 땅을 방문했는지 체크하기 위한 리스트. while문을 돌 때마다 방문 체크 리셋

    for i in range(N):          # 인구이동이 가능한 구간인지 확인하여 visited에 표시
        for j in range(N):
            if visited[i][j]==0 and open(i,j):  # 방문한 적이 없고 인구이동이 가능한 구간이라면
                BFS(i, j)   # 인구이동 시작

print(ans)      # 인구이동 횟수 출력