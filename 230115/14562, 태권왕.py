def bfs(S, T, cnt):
    q = deque()
    q.append((S, T, cnt))
    while q:
        S, T, cnt = q.popleft()
        if S <= T:
            q.append((S+S, T+3, cnt+1))
            q.append((S+1, T, cnt+1))
            if S == T:
                return(cnt)

from collections import deque
import sys
C = int(sys.stdin.readline())
for i in range(C):
    S, T = map(int, sys.stdin.readline().split())
    print(bfs(S, T, 0))