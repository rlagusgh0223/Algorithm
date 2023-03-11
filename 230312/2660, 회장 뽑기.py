def BFS(x):
    q = deque()
    q.append(x)
    ck[x] = 0
    while q:
        x = q.popleft()
        for nx in member[x]:
            if ck[nx] == -1:
                ck[nx] = ck[x] + 1
                q.append(nx)
    return max(ck)

from collections import deque
import sys
N = int(sys.stdin.readline())
member = [[] for _ in range(N)]
ans = [0]*N
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x==-1 and y==-1:
        break
    x, y = x-1, y-1
    member[x].append(y)
    member[y].append(x)
for i in range(N):
    ck = [-1]*N
    ans[i] = BFS(i)
chief = min(ans)
print(chief, ans.count(chief))
result = []
for i in range(N):
    if ans[i] == chief:
        result.append(i+1)
print(*result)