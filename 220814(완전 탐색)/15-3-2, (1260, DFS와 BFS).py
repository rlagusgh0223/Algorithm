from collections import deque
N, M, V = map(int, input().split())
vertex = [[0]*(N+1) for i in range(N+1)]    # 정점과 정점이 연결됨을 저장하기 위한 배열
for i in range(M):
    a, b = map(int, input().split())    # 연결된 정점 a, b를 받는다
    vertex[a][b] = vertex[b][a] = 1    # 상호간에 연결된 부분은 1로 표시한다
visit = [0]*(N+1)    # 방문한 정점은 재방문하지 않기 위해 visit배열을 생성한다

def DFS(V):
    visit[V] = 1    # 방문한 정점은 재방문하지 않도록 1로 설정한다
    print(V, end=' ')    # 방문한 정점 출력
    for i in range(1, N+1):
        if visit[i]==0 and vertex[V][i]==1:    # 해당 정점을 방문하지 않았고 연결되어 있다면
            DFS(i)    # DFS 실행

def BFS(V):
    visit[V] = 0
    queue = deque()
    queue.append(V)
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visit[i]==1 and vertex[V][i]==1:    # DFS에 의해 모든 정점은 방문된 상태이니 visit은 1이다. 이번엔 반대로 0이 방문한 정점이 된다
                queue.append(i)
                visit[i] = 0

DFS(V)
print()
BFS(V)