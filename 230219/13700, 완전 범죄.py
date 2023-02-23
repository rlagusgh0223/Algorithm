def BFS(S):
    q = deque()
    q.append(S)
    b[S] = 0
    while q:
        now = q.popleft()
        if now+F<=N and b[now+F]==-1:
            q.append(now+F)
            b[now+F] = b[now] + 1
        if now-B>0 and b[now-B]==-1:
            q.append(now-B)
            b[now-B] = b[now] + 1
        if now+F==D or now-B==D:
            return b[now]+1
    return "BUG FOUND"

from collections import deque
import sys
N, S, D, F, B, K = map(int, sys.stdin.readline().split())
b = [-1]*(N+1)
for i in map(int, sys.stdin.readline().split()):
    b[i] = -2
print(BFS(S))