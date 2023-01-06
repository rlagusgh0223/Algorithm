def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if ground[x][y] == -1:
            return True
        if x < x+ground[x][y] < N:
            q.append((x+ground[x][y], y))
        if y < y+ground[x][y] < N:
            q.append((x, y+ground[x][y]))
    return False

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
ck = bfs()
if ck:
    print("HaruHaru")
else:
    print("Hing")