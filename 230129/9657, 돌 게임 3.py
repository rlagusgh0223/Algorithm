import sys
N = int(sys.stdin.readline())
dp = [1, 0, 1, 1] + [0]*(N-4)
for i in range(4, N):
    if dp[i-1] == 0:
        dp[i] = 1
    if dp[i-3] == 0:
        dp[i] = 1
    if dp[i-4] == 0:
        dp[i] = 1
if dp[N-1]==1:
    print("SK")
else:
    print("CY")