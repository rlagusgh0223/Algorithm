def BFS(k, v):
    q = deque()
    q.append(v)
    check = [0] * (N+1)
    check[v] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for nxt, score in usado[x]:
            if score>=k and check[nxt]==0:
                q.append(nxt)
                check[nxt] = 1
                cnt += 1
    return cnt

from collections import deque
import sys
N, Q = map(int, sys.stdin.readline().split())
usado = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    usado[p].append((q, r))
    usado[q].append((p, r))
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(BFS(k, v))