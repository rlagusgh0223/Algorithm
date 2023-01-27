def bfs(k):
    q = deque()
    q.append((0, k))  # 정점, 방문 가능 거리
    cnt = apple[0]
    apple[0] = -1
    while q:
        x, k = q.popleft()
        for now in lst[x]:
            if apple[now]!=-1 and k-1>=0:
                q.append((now, k-1))
                cnt += apple[now]
                apple[now] = -1
    return cnt

from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
lst = [[] for x in range(n)]
for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    lst[x].append(y)
    lst[y].append(x)
apple = list(map(int, sys.stdin.readline().split()))
print(bfs(k))