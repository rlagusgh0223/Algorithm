# 한번 더 풀어보기
from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0] * (N+1)
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

def DFS(V):
    visit[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1):
        if visit[i] == 0 and graph[V][i] == 1:
            DFS(i)

def BFS(V):
    visit[V] = 0
    q = deque()
    q.append(V)
    print(V, end = ' ')
    while q:
        V = q.popleft()
        for i in range(1, N+1):
            if visit[i] == 1 and graph[V][i] == 1:
                q.append(i)
                visit[i] = 0
                print(i, end = ' ')

DFS(V)
print()
BFS(V)