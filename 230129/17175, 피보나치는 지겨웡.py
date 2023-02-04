import sys
n = int(sys.stdin.readline())
dp = [1, 1] + [0] * (n-1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] + 1
print(dp[n]%1000000007)