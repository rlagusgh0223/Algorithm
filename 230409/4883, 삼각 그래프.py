# 문제에서 말하는 K는 몇번째 판인지 말하는거다
# N으로 0을 줄 때까지 계속 반복한다
import sys
K = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    # 시작을 가운데 정점에서 하므로 사실상 첫줄은 의미 없다
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp[1][0] += dp[0][1]
    dp[1][1] += min(dp[0][1], dp[0][1]+dp[0][2], dp[1][0])
    dp[1][2] += min(dp[0][1], dp[0][1]+dp[0][2], dp[1][1])
    for i in range(2, N):
        dp[i][0] += min(dp[i-1][0], dp[i-1][1])
        dp[i][1] += min(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][2] += min(dp[i][1], dp[i-1][1], dp[i-1][2])
    print("{}. {}".format(K, dp[N-1][1]))
    K += 1