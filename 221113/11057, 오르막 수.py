import sys
N = int(sys.stdin.readline())
d = [[0]*10 for _ in range(N+1)]
for i in range(10):
    d[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
            d[i][j] %= 10007
print(sum(d[N]) % 10007)