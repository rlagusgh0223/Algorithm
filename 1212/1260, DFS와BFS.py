from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())    #정점의 개수, 간선의 개수, 시작하는 정점
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]   #입력받는 간선들을 이용하여 각 정점은 어느 정점과 연결되어 있는지 표시하는 리스트
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1     #간선을 입력해주면 해당 정점의 리스트에 상대 정점 표시
    graph[b][a] = 1     #ex. 1,3 이면 [1][3], [3][1]에 1 입력

#DFS
def DFS(v):
    visited[v] = True   #탐색하려고 하는 점은 방문한걸로 취급
    print(v, end=' ')   #방문했으니 출력
    for i in range(n+1):    #모든 정점의 수만큼 확인
        if graph[v][i] == 1 and visited[i] == False:    #현재 방문한 정점에서 연결된 정점이 있고, 그 정점을 방문하지 않았다면
            DFS(i)  #재귀함수 이용 그 정점 방문

#BFS
def BFS(v):
    queue = deque()     #큐로 선언
    queue.append(v)     #큐에 시작하는 정점 입력
    visited[v] = True    #시작 정점도 방문한 것이니 방문 체크
    while queue:    #queue가 있는한 반복
        now = queue.popleft()   #queue에 먼저 입력한 순서대로 출력. 처음은 시작점. 그 다음부턴 밑에서 입력되는 정점
        print(now, end=' ')
        for i in range(1, n+1):    #모든 정점의 수만큼 확인
            if graph[now][i] == 1 and visited[i]==False:    #현재 차례인 정점에 연결된 정점이 있고 방문한 적이 없다면
                queue.append(i)     #방문하기 위해 큐에 입력
                visited[i] = True   #현재 정점은 방문했다고 체크하여 다시 오지 않도록 작성

visited = [False] * (n+1)   #방문했는지 표시하는 리스트(정점이 1 ~ n)개 있으니까 n+1개만큼 작성
DFS(v)
print()
visited = [False] * (n+1)
BFS(v)
