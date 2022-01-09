from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
temp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def BFS(x, y):                  # BFS를 이용해 0인 부분 2로 만들기(1이 감싸주지 않는한)
    q = deque()                 # BFS는 1을 세 개 다 세운 후 돌리는 거니까 2로 다 감염될 경우를 만들어준다
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

def get_score():                # 벽을 세우고, 바이러스가 다 퍼지면 괜찮은곳(0)의 갯수를 센다
    global ans
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    ans = max(ans, score)                   # ans는 글로벌 변수로 이전의 안전영역과 현재의 안전영역 중 큰 값을 ans에 준다

def DFS(depth, x, y):                       # depth는 벽의 개수를 의미한다
    if depth == 3:                          # 벽의 개수가 3개면
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]    # 바이러스 전염되는걸 그래프에 그대로 하면 끝나고 돌아오지 않을 것 같아서 동일한 리스트를 만들었다
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:         # 바이러스 구간이면
                    BFS(i, j)               # BFS 동작하여 전염 시작
        get_score()                         # 전염이 끝나면 안전구역 개수 세기
        return

    for i in range(x, n):                   # 재귀함수니까 입력된 좌표부터 벽을 세워야 되므로 x는 입력되는줄 부터 시작되면 된다
        if i == x:                          # 맨 첫 줄은 입력된 좌표의 다음부터 계산해야 되니까 y+1
            for j in range(y+1,m):
                if graph[i][j] == 0:        # 벽 세우고 다음 영역이 0이면
                    graph[i][j] = 1         # 벽 세운다(3번이면 위의 if문에서 BFS 동작한다)
                    DFS(depth+1, i, j)      # DFS를 이용해 다시 반복하고
                    graph[i][j] = 0         # 재귀함수가 끝나면 다시 0으로 만들어준다
        else:                               # 그 다음줄부터는 처음부터 다 반영한다
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    DFS(depth+1, i, j)
                    graph[i][j] = 0

DFS(0,0,-1)         # DFS에서 y+1로 돌아가니까 처음부터 -1을 줘야 0,0에서 시작한다
print(ans)