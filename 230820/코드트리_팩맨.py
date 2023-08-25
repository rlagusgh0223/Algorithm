import sys
m, t = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
ground = [[0]*4 for _ in range(4)]
ground[r-1][c-1] = -1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for _ in range(m):
    r, c, d = map(int, sys.stdin.readline().split())
    ground[r-1][c-1] = d
for i in range(r):
    print(ground[i])