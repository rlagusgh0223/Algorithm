def bfs():
    q = deque()
    q.append(0)
    ck[0] = 0
    while q:
        x = q.popleft()
        for nx, ans in house[x]:
            if ck[nx]==-1:
                ck[nx] = ck[x] + ans
                q.append(nx)
    return max(ck)

from collections import deque
import sys
N = int(sys.stdin.readline())
house = [[] for _ in range(N)]
ck = [-1] * N
for i in range(N-1):
    A, B, C = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1
    house[A].append([B, C])
    house[B].append([A, C])
print(bfs())