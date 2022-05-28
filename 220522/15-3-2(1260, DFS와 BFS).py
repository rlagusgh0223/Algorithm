from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]    # 입력 숫자와 맞추기 위해 1개 더 배열을 만든다
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1
visit = [0]*(N+1)

def DFS(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visit[i] == 0 and graph[V][i] == 1:
            DFS(i)

def BFS(V):
    q = deque()
    q.append(V)
    while q:
        V = q.popleft()
        print(V, end= ' ')
        visit[V] = 0
        for i in range(1, N+1):
            if visit[i] == 1 and graph[V][i] == 1:
                visit[i] = 0
                q.append(i)

DFS(V)
print()
BFS(V)