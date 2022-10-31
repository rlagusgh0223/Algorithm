from collections import deque
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    lst[x][y] = lst[y][x] = 1
chk = []
q = deque()
q.append(1)
cnt = -1
while q:
    now = q.popleft()
    if now not in chk:
        cnt += 1
        chk.append(now)
        for i in range(N+1):
            if lst[now][i]==1:
                q.append(i)
print(cnt)