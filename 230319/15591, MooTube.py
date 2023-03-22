def BFS(k, v):
    q = deque()
    q.append(v)
    check = [0]*(N+1)
    cnt = 0
    check[v] = 1
    while q:
        x = q.popleft()
        for nx, ny in usado[x]:
            if ny>=k and check[nx]==0:
                q.append(nx)
                cnt += 1
                check[nx] = 1
    return cnt

from collections import deque
import sys
N, Q = map(int, sys.stdin.readline().split())
usado = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    usado[a].append((b, c))
    usado[b].append((a, c))
for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(BFS(k, v))  # v가 주어졌을때 유사도 k이상의 값들을 구하는 문제?