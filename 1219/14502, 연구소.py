# 1. 바이러스 구역(2) 주변에 벽(1)으로 에워싸는건 했으나 3번을 넘기므로 답이 아니다
# 2. 3번만 돌아가도록 코드는 작성했으나 다양한 구역에서 돌아가지는 않음
# 3. 반복문 안에 같은 변수(i)를 사용해서 코드에 혼선이 있었음
# 4. 1번과 2번을 융합하려 시도하였으나 실패
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
q = []

def BFS(x, y):
    global cnt
    q = deque()
    q.append([x, y])
    graph[x][y] = 1                 #밑에는 다음 것부터 적용되니까 여기서 시작점 1로 바꾸고 카운터 증가
    cnt += 1
    while q:
        x, y = q.popleft()         #시작점 주변에 점검할 숫자가 있는지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]     
            if cnt % 3 == 0:
                while q:                # whiule문 나가기 전에 3번 벽 세우면 원상복구
                    x, y = q.pop()
                    graph[x][y] = 0
                cnt = 0
            if 0 <= nx < N and 0 <= ny < M:     # 다음 좌표가 그래프 내에 있다면
                if graph[nx][ny]==0:            # 다음 좌표도 조정
                    graph[nx][ny] = 1
                    cnt += 1
                    print(nx, ny)
                    for k in range(N):
                        print(graph[k])
                    print()

for i in range(N):
    for j in range(M):     
        if cnt % 3 == 0:        #3번 벽을 세운 후 리셋하기 위해
            while q:
                x, y = q.pop()
                graph[x][y] = 0
        if graph[i][j] == 0:        # 그래프에서 0이 발견되면
            BFS(i, j)               # 1로 바꾸기 위한 함수 호출
            print("BFS 종료",i, j)  # 호출 후 그래프 확인용
            for k in range(N):
                print(graph[k])
            print()

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