from collections import deque

def DFS(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visit[i] == 0 and spot[V][i] == 1:
            DFS(i)

def BFS(V):
    visit[V] = 0
    q = deque()
    q.append(V)
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visit[i]==1 and spot[V][i]==1:
                q.append(i)
                visit[i] = 0
                
N, M, V = map(int, input().split())
spot = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    spot[x][y] = spot[y][x] = 1
visit = [0] * (N+1)
DFS(V)
print()
BFS(V)