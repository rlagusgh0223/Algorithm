def bfs(x):
    q = deque()
    q.append(x)
    check[x] = 1
    while q:
        x = q.popleft()
        nx1 = x + stone[x]
        nx2 = x - stone[x]
        if 0<=nx1<n and check[nx1]==0:
            check[nx1] = 1
            q.append(nx1)
        if 0<=nx2<n and check[nx2]==0:
            check[nx2] = 1
            q.append(nx2)
    return check.count(1)

from collections import deque
import sys
n = int(sys.stdin.readline())
stone = list(map(int, sys.stdin.readline().split()))
check = [0] * n
s = int(sys.stdin.readline())
print(bfs(s-1))