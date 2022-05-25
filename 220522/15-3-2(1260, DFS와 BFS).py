# 지속적인 공부 필요
from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0] * (N+1)

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] =  graph[y][x] = 1

def DFS(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visit[i]==0 and graph[V][i]==1:
            DFS(i)

def BFS(V):
    q = deque()
    q.append(V)
    visit[V] = 0
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if visit[i] == 1 and graph[V][i]:
                q.append(i)
                visit[i]=0

DFS(V)
print()
BFS(V)