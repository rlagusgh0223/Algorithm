def bfs(x):
    check[x] = True
    q = deque()
    q.append(x)
    while q:
        y = q.popleft()
        for i in graph[y]:
            if not check[i]:
                check[i] = True
                q.append(i)

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[]*(N) for _ in range(N)]
check = [False for _ in range(N)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 0
for i in range(N):
    if not check[i]:
        ans += 1
        bfs(i)
print(ans)