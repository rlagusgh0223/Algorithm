from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)
Max = 200000
dist = [-1] * Max
dist[N] = 0
while q:
    now = q.popleft()
    if now*2<Max and dist[now*2]==-1:
        q.appendleft(now*2)
        dist[now*2] = dist[now]
    if now-1>=0 and dist[now-1]==-1:  # elif로 하면 안된다
        q.append(now-1)
        dist[now-1] = dist[now]+1
    if now+1<Max and dist[now+1]==-1:
        q.append(now+1)
        dist[now+1] = dist[now]+1
print(dist[K])