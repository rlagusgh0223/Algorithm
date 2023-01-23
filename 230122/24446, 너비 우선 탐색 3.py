def bfs(R):
    q = deque()
    q.append(R)
    check[R] = 0
    while q:
        x = q.popleft()
        for nx in lst[x]:
            if check[nx] == -1:
                check[nx] = check[x] + 1
                q.append(nx)

from collections import deque
import sys
input = sys.stdin.readline
N, M ,R = map(int, input().split())
lst = [[] for _ in range(N+1)]
check = [-1] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
bfs(R)
print(*check[1:], sep='\n')