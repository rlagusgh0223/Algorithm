# 내가 생각한것 보다 이 코드가 훨씬 빠르다
def BFS(start, end):
    q = deque()
    q.append((start, 0))
    ck = [0] * (N+1)
    ck[start] = 1
    while q:
        now, cnt = q.popleft()
        if now == end:
            return cnt
        for nx, ncnt in tree[now]:
            if ck[nx] == 0:
                ck[nx] = 1
                q.append((nx, cnt+ncnt))

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x].append((y, z))
    tree[y].append((x, z))
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(BFS(start, end))