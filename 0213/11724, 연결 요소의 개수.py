import sys
sys.setrecursionlimit(10000)    # 재귀함수를 쓸 때는 이렇게 재귀 제한을 풀어줘야 한다

n, m = map(int, sys.stdin.readline().split())    # 접점의 개수와 선의 개수
cnt = 0    # 그래프가 몇개 있는지 계싼하는 변수
graph = [[] for _ in range(n)]    # 각 점별로 연결된 점을 입력하기 위한 리스트
visited = [0] * n    # 각 점들이 연결되 있는 점을 체크했는지 표시하기 위한 리스트

def DFS(x):
    visited[x] = 1    # DFS가 돈다는 것은 방문한다는 의미니까 방문 표시
    for i in graph[x]:    # 현재 점이 다른 점들과 연결되 있는 점 탐색
        if visited[i] == 0:    # 연결된 점이라고 입력받은 점이 다른 점과 연결된 점이 있다면
            DFS(i)    # 재귀함수

for i in range(m):   # 연결된 선을 리스트에 체크하기 위한 반복문
    x, y = map(int, sys.stdin.readline().split())
    x -= 1    # 입력된 값과 리스트의 크기는 다르므로 맞춰서 입력
    y -= 1
    graph[x].append(y)    # 양방향 선이므로 각 점에서 연결 가능한 점을 표시
    graph[y].append(x)

for i in range(n):
    if visited[i] == 0:    # 아직 연결되어 있는지 체크 안한 점이라면
        cnt += 1    # 새로운 그래프가 발생한 것이므로 카운트
        DFS(i)    # 그 점과 연결된 다른 점들 찾는 DFS

print(cnt)



# ===============================================
# 아래는 런타임 에러(RecursionError)가 나는 코드
# 인터넷에서 본걸 참고하여 1차원으로 해보겠다
# import sys

# n, m = map(int, sys.stdin.readline().split())    # 접점의 개수와 선의 개수
# cnt = 0    # 그래프가 몇개 있는지 계싼하는 변수
# visited = [[0 for _ in range(n)] for _ in range(n)]    # 각 점들이 연결되 있는 점을 체크하기 위한 리스트

# def DFS(x, y):
#     visited[x][y] = 2    # DFS가 돈다는 것은 방문한다는 의미니까 방문 표시
#     for i in range(n):    # 각 점이 다른 모든 점들과 연결되있는지 확인하는 반복문
#         if visited[y][i] == 1:    # 연결된 점이라고 입력받은 점이 다른 점과 연결된 점이 있다면
#             DFS(y, i)    # 재귀함수

# for i in range(m):   # 연결된 선을 리스트에 체크하기 위한 반복문
#     x, y = map(int, sys.stdin.readline().split())
#     x -= 1    # 입력된 값과 리스트의 크기는 다르므로 맞춰서 입력
#     y -= 1
#     visited[x][y] = 1    # 방향없는 그래프라고 했으니까 양방향으로 입력
#     visited[y][x] = 1

# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == 1:    # 각 점들 중 연결된 점이 있고, 방문한 적 없으면
#             cnt += 1    # 새로운 그래프가 발생한 것이므로 카운트
#             DFS(i,j)    # 그 점과 연결된 다른 점들 찾는 DFS

# print(cnt)