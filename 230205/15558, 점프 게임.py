def BFS():
    q = deque()
    q.append((0, 0, -1))
    check[0][0] = 1
    while q:
        now, x, cnt = q.popleft()
        if x+1>=N or x+K>=N:
            return 1
        if check[now][x+1]==0 and lst[now][x+1]==1:
            q.append((now, x+1, cnt+1))
            check[now][x+1] = 1
        if x-1>cnt+1 and check[now][x-1]==0 and lst[now][x-1]==1:
            q.append((now, x-1, cnt+1))
            check[now][x-1] = 1
        if check[(now+1)%2][x+K]==0 and lst[(now+1)%2][x+K]==1:
            q.append(((now+1)%2, x+K, cnt+1))
            check[(now+1)%2][x+K] = 1
    return 0

from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
lst = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(2)]
check = [[0]*N for _ in range(2)]
print(BFS())