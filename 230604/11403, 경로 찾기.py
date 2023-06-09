import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j]==1 or(graph[i][k]==1 and graph[k][j]==1):
                graph[i][j] = 1
for now in graph:
    print(*now)