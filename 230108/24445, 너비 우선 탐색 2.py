from collections import deque
import sys
N, M, R = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
ans = [0] * (N+1)
cnt = 0
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)
q = deque()
q.append(R)
while q:
    x = q.popleft()
    if ans[x] == 0:
        cnt += 1
        ans[x] = cnt
        lst[x].sort(reverse=True)
        for nx in lst[x]:
            q.append(nx)
for i in range(1, N+1):
    print(ans[i])