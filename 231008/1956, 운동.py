# pypy3로 해야된다
import sys
V, E = map(int, sys.stdin.readline().split())
graph = [[int(1e9)]*V for _ in range(V)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
ans = int(1e9)
for i in range(V):
    # 사이클은 자기 자신으로 돌아오는 길을 말한다
    ans = min(ans, graph[i][i])
if ans == int(1e9):
    print(-1)
else:
    print(ans)