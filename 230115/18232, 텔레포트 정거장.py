def bfs(S):
    q = deque()
    q.append(S)
    check[S] = 0
    while q:
        S = q.popleft()
        if S == E:
            return check[S]
        if 1<=S<N and check[S+1] == -1:
            q.append(S+1)
            check[S+1] = check[S] + 1
        if 0<S<=N and check[S-1] == -1:
            q.append(S-1)
            check[S-1] = check[S] + 1
        for i in port[S]:
            if check[i] == -1:
                q.append(i)
                check[i] = check[S] + 1

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S, E = map(int, input().split())
port = [[] for _ in range(N+1)]
check = [-1] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    port[x].append(y)
    port[y].append(x)
print(bfs(S))