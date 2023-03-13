import sys
N = int(sys.stdin.readline())
dp = [[0, []] for _ in range(N+1)]
dp[1][1] = [1]
for i in range(2, N+1):
    dp[i][0]  = dp[i-1][0]+1  # 한 줄로 하는것보단 이게 가독성이 높은것 같아서 두 줄로 나눠 썼다
    dp[i][1] = dp[i-1][1]+[i]
    if i%2==0 and dp[i][0]>dp[i//2][0]+1:
        dp[i][0] = dp[i//2][0]+1
        dp[i][1] = dp[i//2][1]+[i]
    if i%3==0 and dp[i][0]>dp[i//3][0]+1:
        dp[i][0] = dp[i//3][0]+1
        dp[i][1] = dp[i//3][1]+[i]
print(dp[N][0])
print(*sorted(dp[N][1], reverse=True))