import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[0]*N for _ in range(N)]
for i in range(N):
    d[i][i] = True
for i in range(N-1):
    if a[i] == a[i+1]:
        d[i][i+1] = True
for k in range(3, N+1):
    for i in range(N+1-k):
        j = i+k-1
        if a[i]==a[j] and d[i+1][j-1]:
            d[i][j] = True
M = int(sys.stdin.readline())
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(1 if d[s-1][e-1] else 0)