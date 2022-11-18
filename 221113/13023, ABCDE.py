import sys
N, M = map(int, sys.stdin.readline().split())
edges = []
a = [[False]*N for _ in range(N)]
d = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    edges.append((x, y))
    edges.append((y, x))
    a[x][y] = a[y][x] = True
    d[x].append(y)
    d[y].append(x)
M *= 2
for i in range(M):
    for j in range(M):
        A, B = edges[i]
        C, D = edges[j]
        if A==B or A==C or A==D or B==C or B==D or C==D:
            continue
        if not a[B][C]:
            continue
        for E in d[D]:
            if A==E or B==E or C==E or D==E:
                continue
            print(1)
            sys.exit(0)
print(0)