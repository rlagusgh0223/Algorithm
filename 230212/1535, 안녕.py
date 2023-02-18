# 냅색 알고리즘
import sys
N = int(sys.stdin.readline())
L = [0] + list(map(int, sys.stdin.readline().split()))
J = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0]*101 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][99])