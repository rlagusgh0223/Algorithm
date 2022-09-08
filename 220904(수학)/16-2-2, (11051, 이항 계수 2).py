N, K = map(int, input().split())
dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):
    for j in range(i+1):
        if j==0 or j==i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[N][K])