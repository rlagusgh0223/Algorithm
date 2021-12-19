from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
q = []

for i in range(N):
    for j in range(M):        
        if cnt % 3 == 0:
            while q:
                x, y = q.pop()
                graph[x][y] = 0
        if graph[i][j] == 0:
            print('하나시작',i,j)
            for k in range(N):
                print(graph[k])
            print()
            cnt += 1
            graph[i][j] = 1
            q.append([i,j])
            for k in range(N):
                print(graph[k])
            print()
            a = input()