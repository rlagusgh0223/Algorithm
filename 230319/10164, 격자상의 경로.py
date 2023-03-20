import sys
N, M, K = map(int, sys.stdin.readline().split())
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][1], cnt = 1, 0
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt += 1
        if cnt == K:
            x, y = i, j
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
if K == 0:
    print(dp[N][M])
else:
    # O를 반드시 거쳐야 한다는 말은 거기서 시작한다는 뜻이다
    # O까지 오는 경우의 수와
    # O에서 출발하여 NM까지 오는 경우의 수를 곱하면 된다
    # O에서 출발하여 NM까지 오는 경우의 수는
    # 1,1 에서 출발하여 N-x+1, M-y+1로 오는 경우의 수와 같다
    print(dp[x][y] * dp[N-x+1][M-y+1])