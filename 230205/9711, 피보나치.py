import sys
dp = [0, 1, 1] + [0]*(10000-2)
for i in range(3, 10001):
    dp[i] = dp[i-1] + dp[i-2]
T = int(sys.stdin.readline())
for i in range(1, T+1):
    P, Q = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, dp[P]%Q))