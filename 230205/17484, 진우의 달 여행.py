import sys
N, M = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[sys.maxsize]*3 for _ in range(M)] for _ in range(N)]
for i in range(N):
    if i == 0:
        for j in range(M):
            for k in range(3):
                dp[i][j][k] = lst[i][j]
    else:
        for j in range(M):
            if j == 0:
                dp[i][j][1] = dp[i-1][j][2] + lst[i][j]
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + lst[i][j]
            elif j == M-1:
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + lst[i][j]
                dp[i][j][1] = dp[i-1][j][0] + lst[i][j]
            else:
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + lst[i][j]
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + lst[i][j]
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + lst[i][j]
ans = sys.maxsize
for i in range(M):
    ans = min(min(dp[N-1][i]), ans)
print(ans)