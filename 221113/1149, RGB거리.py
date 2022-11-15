import sys
N = int(sys.stdin.readline())
d = [[0] for _ in range(N)]
for i in range(N):
    d[i] = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + d[i][2]
print(min(d[N-1]))