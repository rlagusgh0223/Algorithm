from collections import deque
import sys
N = int(sys.stdin.readline())
C = int(sys.stdin.readline())
lst = [[0]*(N+1) for _ in range(N+1)]
for i in range(C):
    x, y = map(int, sys.stdin.readline().split())
    lst[x][y] = lst[y][x] = 1
visit = [True]*(N+1)
q = deque()
q.append(1)
visit[1] = False
cnt = 0
while q:
    now = q.popleft()
    for i in range(1, N+1):
        if lst[now][i] == 1 and visit[i]:
            visit[i] = False
            q.append(i)
            cnt += 1
print(cnt)