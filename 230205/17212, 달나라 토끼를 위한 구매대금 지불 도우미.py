import sys
N = int(sys.stdin.readline())
dp = [0,1,1,2,2,1,2,1] + [0]*(N-7)
for i in range(8, N+1):
    dp[i] = min(dp[i-7], dp[i-5], dp[i-2], dp[i-1])+1
print(dp[N])