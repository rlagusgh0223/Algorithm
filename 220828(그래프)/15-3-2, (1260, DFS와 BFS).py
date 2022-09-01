from collections import deque
import sys

def DFS(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visit[i]==0 and graph[V][i]==1:
            DFS(i)

def BFS(V):
    visit[V] = 0
    q = deque()
    q.append(V)
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visit[i]==1 and graph[V][i]==1:
                visit[i] = 0
                q.append(i)

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [0] * (N+1)
DFS(V)
print()
BFS(V)