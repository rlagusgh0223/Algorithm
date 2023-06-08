import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)  # 각 금액별 가능한 경우의 수
    dp[0] = 1  # i==coin일때 i-coin을 하면 0이 되므로 어떤 동전이던 0의 값은 존재한다
    for coin in coins:
        for i in range(M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])