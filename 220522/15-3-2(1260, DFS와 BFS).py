from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
lst = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0] * (N+1)
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    lst[x][y] = lst[y][x] = 1

def DFS(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(N+1):
        if visit[i] == 0 and lst[V][i] == 1:
            DFS(i)

def BFS(V):
    q = deque()
    q.append(V)
    while q:
        V = q.popleft()
        visit[V] = 0
        print(V, end=' ')
        for i in range(N+1):
            if visit[i] == 1 and lst[V][i] == 1:
                q.append(i)
                visit[i] = 0

DFS(V)
print()
BFS(V)