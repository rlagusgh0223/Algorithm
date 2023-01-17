def bfs(a):
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        for i in range(N):
            if (i-x)%lst[x]==0 and check[i]==-1:
                check[i] = check[x] + 1
                q.append(i)
                if i == b:
                    return check[i]
    return -1

from collections import deque
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
a -= 1
b -= 1
check = [-1] * N
check[a] = 0
print(bfs(a))