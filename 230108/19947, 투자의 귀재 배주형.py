import sys
H, Y = map(int, sys.stdin.readline().split())
dp = [H] + [0]*Y
for i in range(1, Y+1):
    if i < 3:
        dp[i] = int(dp[i-1]*1.05)
    elif i < 5:
        dp[i] = max(int(dp[i-1]*1.05), int(dp[i-3]*1.2))
    else:
        dp[i] = max(int(dp[i-1]*1.05), int(dp[i-3]*1.2), int(dp[i-5]*1.35))
print(dp[Y])