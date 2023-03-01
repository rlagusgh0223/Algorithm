# 50m당 하나씩 20개이므로 1000m까지 행복하게 갈 수 있다
def BFS(home):
    q = deque()
    q.append(home)
    while q:
        x, y = q.popleft()
        if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
            return "happy"
        for i in range(n):
            if visit[i]==0:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append((nx, ny))
                    visit[i] = 1
    return "sad"

from collections import deque
import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    fest = list(map(int, sys.stdin.readline().split()))
    visit = [0] * n
    print(BFS(home))