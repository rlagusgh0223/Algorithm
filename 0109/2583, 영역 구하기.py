from collections import deque
import sys

N, M, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
search = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이렇게 짜면 문제에서 원하는 것과는 위아래 대칭되지만,
# 문제가 빈 공간의 개수와 면적을 구하는 것이므로 문제 푸는데는 문제 없을걸로 판단했다
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1
        
result = []     # 빈 공간의 면적을 입력할 리스트
cnt = 0         # 빈 공간의 개수를 입력할 변수

def BFS(x,y):
    score = 1           # BFS에 들어왔다는 것이 일단 빈 공간이 하나는 있다는 소리니까 1부터 시작
    graph[x][y] = -1    # visited로 방문을 표시하는 대신 graph에 -1을 넣어서 방문을 표시했다
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    score += 1
                    graph[nx][ny] = -1
    return score

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            cnt += 1            # 0이 하나 새로 발견되면 새로운 빈 공간이 발생했으므로 1개 더한다
            s = BFS(i,j)
            result.append(s)    # 리턴받은 빈 공간의 면적을 입력한다
result.sort()                   # 빈 공간의 면적을 오름차순으로 정렬
print(cnt)
for i in result:                # result자체를 출력하면 예제 출력처럼 나오지 않으므로
    print(i, end=' ')