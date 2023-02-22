# 모든 수에 대해 small world가 적용되는지 확인해야 한다
def BFS(x):
    q = deque()
    q.append(x)
    ck[x] = 0
    while q:
        x = q.popleft()
        for nx in friend[x]:
            if ck[nx] == -1:
                ck[nx] = ck[x] + 1
                q.append(nx)
    if min(ck)==-1 or max(ck)>6:
        return True
    else:
        return False

from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
friend = [[] for _ in range(N)]
for i in range(K):
    A, B = map(int, sys.stdin.readline().split())
    A, B = A-1, B-1
    friend[A].append(B)
    friend[B].append(A)
for i in range(N):
    ck = [-1] * N
    if BFS(i):
        print("Big World!")
        exit()
print("Small World!")