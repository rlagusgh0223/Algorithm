import sys
N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        d[i][j] = max(d[i-1][j], d[i][j-1]) + a[i-1][j-1]
print(d[N][M])