import sys
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    dp = [[0, 0]]*41
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    now = [0, 0]
    for i in range(2, N+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    print(dp[N][0], dp[N][1])