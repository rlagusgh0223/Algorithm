from collections import deque
import sys
S = int(sys.stdin.readline())
q = deque()
q.append((1, 0))
dist = [[-1]*(S+1) for _ in range(S+1)]
dist[1][0] = 0

while q:
    s, c = q.popleft()
    if dist[s][s]==-1:
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    if s+c<=S and dist[s+c][c]==-1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1>=0 and dist[s-1][c]==-1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
ans = 0
for i in range(S+1):
    if dist[S][i] != -1:
        if ans==0 or ans>dist[S][i]:
            ans = dist[S][i]
print(ans)