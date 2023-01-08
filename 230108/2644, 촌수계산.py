from collections import deque
def bfs():
    q = deque()
    q.append((start, 1))  # 현재 사람, 촌수
    while q:
        x, cnt = q.popleft()
        if family[x][end] == 1:
            return cnt
        for i in range(1, n+1):
            if family[x][i] == 1:
                q.append((i, cnt+1))
                family[x][i] = cnt+1
    return -1

import sys
input = sys.stdin.readline
n = int(input())
start, end = map(int, input().split())  # 촌수 계산
m = int(input())
family = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    family[x][y] = family[y][x] = 1
print(bfs())